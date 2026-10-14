import base64
import hashlib
import json
import re
from pathlib import Path

from cryptography.hazmat.primitives.ciphers.aead import AESGCM

from tools.manual_publisher.protect_static_pages import (
    PROTECTED_PAGE_MARKER,
    UNLOCK_VERIFIER_TEXT,
    encrypt_html,
    find_selected_pages,
    inject_global_unlock_ui,
    protect_selected_pages,
    protect_html_file,
    prune_search_index,
)


def decrypt_payload(payload: dict[str, str | int], password: str) -> str:
    salt = base64.b64decode(str(payload["salt"]))
    iv = base64.b64decode(str(payload["iv"]))
    ciphertext = base64.b64decode(str(payload["ciphertext"]))
    key = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode("utf-8"),
        salt,
        int(payload["iterations"]),
        dklen=32,
    )
    return AESGCM(key).decrypt(iv, ciphertext, None).decode("utf-8")


def extract_payload(protected_html: str) -> dict[str, str | int]:
    match = re.search(
        r'<script type="application/json" id="ars-protected-page-data">(?P<payload>.*?)</script>',
        protected_html,
        re.DOTALL,
    )
    assert match is not None
    return json.loads(match.group("payload"))


def write_html(path: Path, title: str = "Pagina", body: str = "Contenuto") -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(f"<html><head><title>{title}</title></head><body>{body}</body></html>", encoding="utf-8")


def write_theme_page(path: Path, body: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        "\n".join(
            [
                "<html>",
                "<head><title>Pagina</title></head>",
                "<body>",
                '<div class="article-header-buttons">',
                '<button class="btn">Altro</button>',
                "</div>",
                body,
                "</body>",
                "</html>",
            ]
        ),
        encoding="utf-8",
    )


def test_finds_only_explicitly_selected_pages(tmp_path: Path):
    root = tmp_path / "build"
    write_html(root / "V. 1.0" / "IT" / "FlexiBowl_manual" / "MANUTENZIONE" / "02_straordinaria.html")
    write_html(root / "V. 1.0" / "IT" / "FlexiBowl_manual" / "MANUTENZIONE" / "02-1_sost-backlight.html")
    write_html(root / "V. 1.0" / "IT" / "FlexiBowl_manual" / "MANUTENZIONE" / "01_ordinaria.html")
    write_html(root / "V. 1.0" / "IT" / "FlexiBowl_manual" / "TRAMOGGE" / "manutenzione.html")

    docnames = {
        page.docname
        for page in find_selected_pages(
            root,
            [
                "V. 1.0/IT/FlexiBowl_manual/MANUTENZIONE/02_straordinaria.html",
                r"V. 1.0\IT\FlexiBowl_manual\TRAMOGGE\manutenzione.html",
                "../outside.html",
            ],
        )
    }

    assert docnames == {
        "FlexiBowl_manual/MANUTENZIONE/02_straordinaria",
        "FlexiBowl_manual/TRAMOGGE/manutenzione",
    }


def test_protect_html_file_removes_plaintext_and_keeps_decryptable_payload(tmp_path: Path):
    html_file = tmp_path / "page.html"
    original_html = (
        "<html><head><title>Segreto</title></head>"
        "<body><h1>Sostituzione Backlight</h1><p>Testo riservato</p></body></html>"
    )
    html_file.write_text(original_html, encoding="utf-8")

    assert protect_html_file(html_file, "ArS2026!") is True

    protected_html = html_file.read_text(encoding="utf-8")
    assert PROTECTED_PAGE_MARKER in protected_html
    assert "Segreto" not in protected_html
    assert "Testo riservato" not in protected_html
    assert "Sostituzione Backlight" not in protected_html
    assert decrypt_payload(extract_payload(protected_html), "ArS2026!") == original_html


def test_encryption_rejects_wrong_password():
    payload = encrypt_html("contenuto", "ArS2026!")

    try:
        decrypt_payload(payload, "password-sbagliata")
    except Exception:
        return

    raise AssertionError("Payload decrypted with the wrong password")


def test_inject_global_unlock_ui_hides_protected_nav_links(tmp_path: Path):
    root = tmp_path / "build"
    index = root / "V. 1.0" / "IT" / "index.html"
    write_theme_page(
        index,
        """
<ul class="nav bd-sidenav">
<li class="toctree-l1"><a class="reference internal" href="FlexiBowl_manual/MANUTENZIONE/01_ordinaria.html">Ordinaria</a></li>
<li class="toctree-l1"><a class="reference internal" href="FlexiBowl_manual/MANUTENZIONE/02_straordinaria.html">Straordinaria</a></li>
</ul>
""",
    )
    verifier = encrypt_html(UNLOCK_VERIFIER_TEXT, "ArS2026!")

    changed = inject_global_unlock_ui(
        index,
        root,
        {"V. 1.0/IT/FlexiBowl_manual/MANUTENZIONE/02_straordinaria.html"},
        verifier,
    )

    html = index.read_text(encoding="utf-8")
    assert changed is True
    assert 'data-ars-protected-access-button' in html
    assert 'id="ars-protected-access-dialog"' in html
    assert 'id="ars-protected-access-style"' in html
    assert 'data-ars-protected-link-wrapper="true"' in html
    assert 'data-ars-protected-link="true" class="reference internal" href="FlexiBowl_manual/MANUTENZIONE/02_straordinaria.html"' in html
    assert 'data-ars-protected-link="true" class="reference internal" href="FlexiBowl_manual/MANUTENZIONE/01_ordinaria.html"' not in html


def test_prune_search_index_removes_protected_doc_and_terms(tmp_path: Path):
    language_root = tmp_path / "build" / "V. 1.0" / "IT"
    language_root.mkdir(parents=True)
    search_index = language_root / "searchindex.js"
    payload = {
        "docnames": [
            "FlexiBowl_manual/MANUTENZIONE/01_ordinaria",
            "FlexiBowl_manual/MANUTENZIONE/02_straordinaria",
            "FlexiBowl_manual/ALTRO/pagina",
        ],
        "filenames": ["01_ordinaria.html", "02_straordinaria.html", "pagina.html"],
        "titles": ["Ordinaria", "Straordinaria", "Pagina"],
        "terms": {
            "comune": [0, 1, 2],
            "segreto": 1,
            "altro": 2,
        },
        "titleterms": {
            "manutenzione": [0, 1],
            "straordinaria": 1,
        },
        "alltitles": {
            "Titolo segreto": [[1, "titolo-segreto"]],
            "Titolo altro": [[2, "titolo-altro"]],
        },
    }
    search_index.write_text("Search.setIndex(" + json.dumps(payload) + ")", encoding="utf-8")

    changed = prune_search_index(language_root, {"FlexiBowl_manual/MANUTENZIONE/02_straordinaria"})

    assert changed is True
    updated = json.loads(search_index.read_text(encoding="utf-8").removeprefix("Search.setIndex(").removesuffix(")"))
    assert updated["docnames"] == [
        "FlexiBowl_manual/MANUTENZIONE/01_ordinaria",
        "FlexiBowl_manual/ALTRO/pagina",
    ]
    assert updated["titles"] == ["Ordinaria", "Pagina"]
    assert updated["terms"] == {"comune": [0, 1], "altro": 1}
    assert updated["titleterms"] == {"manutenzione": [0]}
    assert updated["alltitles"] == {"Titolo altro": [[1, "titolo-altro"]]}


def test_protect_selected_pages_prunes_search(tmp_path: Path):
    root = tmp_path / "build"
    language_root = root / "V. 1.0" / "IT"
    target = language_root / "FlexiBowl_manual" / "MANUTENZIONE" / "02_straordinaria.html"
    ordinary = language_root / "FlexiBowl_manual" / "MANUTENZIONE" / "01_ordinaria.html"
    index = language_root / "index.html"
    write_html(target, "Straordinaria", "Segreto tecnico")
    write_html(ordinary, "Ordinaria", "Contenuto pubblico")
    write_theme_page(
        index,
        '<li class="toctree-l1"><a class="reference internal" href="FlexiBowl_manual/MANUTENZIONE/02_straordinaria.html">Straordinaria</a></li>',
    )
    (language_root / "searchindex.js").write_text(
        "Search.setIndex("
        + json.dumps(
            {
                "docnames": [
                    "FlexiBowl_manual/MANUTENZIONE/01_ordinaria",
                    "FlexiBowl_manual/MANUTENZIONE/02_straordinaria",
                ],
                "filenames": ["01_ordinaria.html", "02_straordinaria.html"],
                "titles": ["Ordinaria", "Straordinaria"],
                "terms": {"pubblico": 0, "segreto": 1},
                "titleterms": {"ordinaria": 0, "straordinaria": 1},
                "alltitles": {},
            }
        )
        + ")",
        encoding="utf-8",
    )

    protected_count = protect_selected_pages(
        root,
        ["V. 1.0/IT/FlexiBowl_manual/MANUTENZIONE/02_straordinaria.html"],
        password="ArS2026!",
    )

    assert protected_count == 1
    assert PROTECTED_PAGE_MARKER in target.read_text(encoding="utf-8")
    assert "Segreto tecnico" not in target.read_text(encoding="utf-8")
    assert "Contenuto pubblico" in ordinary.read_text(encoding="utf-8")
    assert 'data-ars-protected-access-button' in index.read_text(encoding="utf-8")
    assert 'data-ars-protected-link-wrapper="true"' in index.read_text(encoding="utf-8")
    search_index = (language_root / "searchindex.js").read_text(encoding="utf-8")
    assert "02_straordinaria" not in search_index
    assert "segreto" not in search_index
