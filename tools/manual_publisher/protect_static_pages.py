from __future__ import annotations

import base64
import hashlib
import json
import os
import re
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path, PurePosixPath
from urllib.parse import unquote, urlsplit

from cryptography.hazmat.primitives.ciphers.aead import AESGCM

DEFAULT_PROTECTED_PAGE_PASSWORD = "ArS2026!"
PROTECTED_PAGE_PASSWORD_ENV = "FLEXIBOWL_PROTECTED_PAGE_PASSWORD"
PROTECTED_PAGE_MARKER = '<meta name="ars-protected-page" content="encrypted">'
GLOBAL_UNLOCK_STYLE_RE = re.compile(
    r"\n?\s*<style id=\"ars-protected-access-style\">.*?</style>",
    re.DOTALL,
)
GLOBAL_UNLOCK_SCRIPT_RE = re.compile(
    r"\n?\s*<script id=\"ars-protected-access-script\">.*?</script>",
    re.DOTALL,
)
GLOBAL_UNLOCK_DIALOG_RE = re.compile(
    r"\n?\s*<dialog id=\"ars-protected-access-dialog\".*?</dialog>",
    re.DOTALL,
)
GLOBAL_UNLOCK_BUTTON_RE = re.compile(
    r"\n?\s*<button\b(?=[^>]*\bdata-ars-protected-access-button\b)[\s\S]*?</button>",
    re.DOTALL,
)
ANCHOR_RE = re.compile(r"<a\b(?P<attrs>[^>]*\bhref=(?P<quote>[\"'])(?P<href>.*?)(?P=quote)[^>]*)>", re.DOTALL)
PROTECTED_NAV_ITEM_RE = re.compile(
    r"(<li\b(?![^>]*\bdata-ars-protected-link-wrapper=)(?P<attrs>[^>]*)>\s*)"
    r"(<a\b(?=[^>]*\bdata-ars-protected-link=\"true\")[^>]*>)",
    re.DOTALL,
)
PBKDF2_ITERATIONS = 250_000
SALT_SIZE = 16
IV_SIZE = 12
UNLOCK_VERIFIER_TEXT = "ars-protected-access-ok"

SEARCH_INDEX_RE = re.compile(r"^\s*Search\.setIndex\((?P<payload>.*)\)\s*;?\s*$", re.DOTALL)


@dataclass(frozen=True)
class ProtectedPage:
    html_file: Path
    language_root: Path
    docname: str


def normalize_page_spec(page_spec: str) -> str:
    normalized = page_spec.strip().replace("\\", "/").lstrip("/")
    if normalized.lower().endswith(".md"):
        normalized = normalized[:-3] + ".html"
    return normalized


def get_protected_page_password() -> str:
    return os.environ.get(PROTECTED_PAGE_PASSWORD_ENV) or DEFAULT_PROTECTED_PAGE_PASSWORD


def find_language_root(html_file: Path, site_root: Path) -> Path | None:
    try:
        resolved_root = site_root.resolve()
        relative_parts = html_file.resolve().relative_to(resolved_root).parts
    except ValueError:
        return None

    for index, part in enumerate(relative_parts):
        if part == "FlexiBowl_manual" and index >= 2:
            return resolved_root.joinpath(*relative_parts[:index])

    return None


def resolve_selected_html_file(site_root: Path, page_spec: str) -> Path | None:
    normalized = normalize_page_spec(page_spec)
    if not normalized or not normalized.lower().endswith(".html"):
        return None

    relative_path = Path(*PurePosixPath(normalized).parts)
    candidate = (site_root / relative_path).resolve()
    resolved_root = site_root.resolve()

    try:
        candidate.relative_to(resolved_root)
    except ValueError:
        return None

    if not candidate.exists() or not candidate.is_file():
        return None

    return candidate


def find_selected_pages(site_root: Path, page_specs: list[str]) -> list[ProtectedPage]:
    selected_pages: list[ProtectedPage] = []
    seen: set[Path] = set()

    for page_spec in page_specs:
        html_file = resolve_selected_html_file(site_root, page_spec)
        if html_file is None or html_file in seen:
            continue

        language_root = find_language_root(html_file, site_root)
        if language_root is None:
            continue

        docname = html_file.relative_to(language_root).with_suffix("").as_posix()
        selected_pages.append(ProtectedPage(html_file, language_root, docname))
        seen.add(html_file)

    return selected_pages


def encrypt_html(html: str, password: str) -> dict[str, str | int]:
    salt = os.urandom(SALT_SIZE)
    iv = os.urandom(IV_SIZE)
    key = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt, PBKDF2_ITERATIONS, dklen=32)
    ciphertext = AESGCM(key).encrypt(iv, html.encode("utf-8"), None)
    return {
        "version": 1,
        "algorithm": "AES-GCM",
        "kdf": "PBKDF2-SHA256",
        "iterations": PBKDF2_ITERATIONS,
        "salt": base64.b64encode(salt).decode("ascii"),
        "iv": base64.b64encode(iv).decode("ascii"),
        "ciphertext": base64.b64encode(ciphertext).decode("ascii"),
    }


def render_global_unlock_style() -> str:
    return """  <style id="ars-protected-access-style">
    html:not([data-ars-protected-unlocked="true"]) [data-ars-protected-link-wrapper="true"],
    html:not([data-ars-protected-unlocked="true"]) a[data-ars-protected-link="true"] {
      display: none !important;
    }
    .ars-protected-access-dialog {
      width: min(390px, calc(100vw - 32px));
      border: 1px solid rgba(23, 32, 51, 0.18);
      border-radius: 8px;
      padding: 0;
      color: var(--pst-color-text-base, #172033);
      background: var(--pst-color-background, #fff);
      box-shadow: 0 22px 70px rgba(20, 31, 54, 0.22);
    }
    .ars-protected-access-dialog::backdrop {
      background: rgba(10, 16, 28, 0.42);
    }
    .ars-protected-access-form {
      padding: 24px;
    }
    .ars-protected-access-form h2 {
      margin: 0 0 8px;
      font-size: 1.12rem;
      line-height: 1.25;
    }
    .ars-protected-access-form p {
      margin: 0 0 18px;
      color: var(--pst-color-text-muted, #536071);
      line-height: 1.42;
    }
    .ars-protected-access-form label {
      display: block;
      margin-bottom: 7px;
      font-weight: 650;
      font-size: 0.9rem;
    }
    .ars-protected-access-form input {
      box-sizing: border-box;
      width: 100%;
      min-height: 40px;
      padding: 8px 10px;
      border: 1px solid var(--pst-color-border, #b9c2cf);
      border-radius: 6px;
      color: inherit;
      background: var(--pst-color-background, #fff);
      font: inherit;
    }
    .ars-protected-access-actions {
      display: flex;
      justify-content: flex-end;
      gap: 10px;
      margin-top: 18px;
    }
    .ars-protected-access-error {
      min-height: 1.3em;
      margin-top: 10px;
      color: #b3261e;
      font-size: 0.9rem;
    }
  </style>"""


def render_global_unlock_button() -> str:
    return """<button type="button"
  class="btn btn-sm pst-navbar-icon ars-protected-access-button pst-js-only"
  title="Sblocca contenuti riservati"
  aria-label="Sblocca contenuti riservati"
  data-bs-placement="bottom" data-bs-toggle="tooltip"
  data-ars-protected-access-button>
  <span class="btn__icon-container">
    <i class="fas fa-lock"></i>
  </span>
</button>
"""


def render_global_unlock_dialog() -> str:
    return """  <dialog id="ars-protected-access-dialog" class="ars-protected-access-dialog">
    <form id="ars-protected-access-form" class="ars-protected-access-form">
      <h2>Contenuti riservati</h2>
      <p>Inserisci la password per mostrare le pagine protette nell'indice.</p>
      <label for="ars-protected-access-password">Password</label>
      <input id="ars-protected-access-password" type="password" autocomplete="current-password" required>
      <div id="ars-protected-access-error" class="ars-protected-access-error" role="alert" aria-live="polite"></div>
      <div class="ars-protected-access-actions">
        <button type="button" class="btn btn-sm btn-secondary" data-ars-protected-access-close>Annulla</button>
        <button type="submit" class="btn btn-sm btn-primary" id="ars-protected-access-submit">Sblocca</button>
      </div>
    </form>
  </dialog>"""


def render_global_unlock_script(verifier_payload: dict[str, str | int]) -> str:
    verifier_json = json.dumps(verifier_payload, ensure_ascii=False, separators=(",", ":"))
    return f"""  <script id="ars-protected-access-script">
    (() => {{
      "use strict";

      const verifier = {verifier_json};
      const expectedText = {json.dumps(UNLOCK_VERIFIER_TEXT)};
      const storageKey = "arsProtectedPagePassword";
      const encoder = new TextEncoder();
      const decoder = new TextDecoder();

      function b64ToBytes(value) {{
        const binary = atob(value);
        const bytes = new Uint8Array(binary.length);
        for (let i = 0; i < binary.length; i += 1) {{
          bytes[i] = binary.charCodeAt(i);
        }}
        return bytes;
      }}

      async function deriveKey(password, salt, iterations) {{
        const passwordKey = await crypto.subtle.importKey(
          "raw",
          encoder.encode(password),
          "PBKDF2",
          false,
          ["deriveKey"]
        );
        return crypto.subtle.deriveKey(
          {{
            name: "PBKDF2",
            salt,
            iterations,
            hash: "SHA-256"
          }},
          passwordKey,
          {{ name: "AES-GCM", length: 256 }},
          false,
          ["decrypt"]
        );
      }}

      async function verifyPassword(password) {{
        const salt = b64ToBytes(verifier.salt);
        const iv = b64ToBytes(verifier.iv);
        const ciphertext = b64ToBytes(verifier.ciphertext);
        const key = await deriveKey(password, salt, verifier.iterations);
        const clearBytes = await crypto.subtle.decrypt({{ name: "AES-GCM", iv }}, key, ciphertext);
        return decoder.decode(clearBytes) === expectedText;
      }}

      function getSavedPassword() {{
        try {{
          return sessionStorage.getItem(storageKey);
        }} catch (_) {{
          return null;
        }}
      }}

      function savePassword(password) {{
        try {{
          sessionStorage.setItem(storageKey, password);
        }} catch (_) {{
        }}
      }}

      function forgetPassword() {{
        try {{
          sessionStorage.removeItem(storageKey);
        }} catch (_) {{
        }}
      }}

      function setUnlocked(unlocked) {{
        document.documentElement.dataset.arsProtectedUnlocked = unlocked ? "true" : "false";
        document.querySelectorAll("[data-ars-protected-access-button] i").forEach((icon) => {{
          icon.classList.toggle("fa-lock", !unlocked);
          icon.classList.toggle("fa-unlock", unlocked);
        }});
        document.querySelectorAll("[data-ars-protected-access-button]").forEach((button) => {{
          const label = unlocked ? "Contenuti riservati sbloccati" : "Sblocca contenuti riservati";
          button.setAttribute("title", label);
          button.setAttribute("aria-label", label);
        }});
      }}

      function setError(message) {{
        const errorBox = document.getElementById("ars-protected-access-error");
        if (errorBox) {{
          errorBox.textContent = message;
        }}
      }}

      function openDialog() {{
        const dialog = document.getElementById("ars-protected-access-dialog");
        const passwordInput = document.getElementById("ars-protected-access-password");
        setError("");
        if (!window.crypto || !crypto.subtle) {{
          setError("Apri il manuale tramite HTTPS o localhost per usare lo sblocco.");
          return;
        }}
        if (document.documentElement.dataset.arsProtectedUnlocked === "true") {{
          return;
        }}
        if (dialog && typeof dialog.showModal === "function") {{
          dialog.showModal();
          if (passwordInput) {{
            passwordInput.focus();
          }}
          return;
        }}
        const password = window.prompt("Password contenuti riservati");
        if (password) {{
          unlockWithPassword(password);
        }}
      }}

      async function unlockWithPassword(password) {{
        const submitButton = document.getElementById("ars-protected-access-submit");
        if (submitButton) {{
          submitButton.disabled = true;
        }}
        setError("");
        try {{
          if (!(await verifyPassword(password))) {{
            throw new Error("Invalid password");
          }}
          savePassword(password);
          setUnlocked(true);
          const dialog = document.getElementById("ars-protected-access-dialog");
          if (dialog && typeof dialog.close === "function") {{
            dialog.close();
          }}
        }} catch (_) {{
          forgetPassword();
          setUnlocked(false);
          const passwordInput = document.getElementById("ars-protected-access-password");
          if (passwordInput) {{
            passwordInput.select();
          }}
          setError("Password non valida.");
        }} finally {{
          if (submitButton) {{
            submitButton.disabled = false;
          }}
        }}
      }}

      document.addEventListener("DOMContentLoaded", () => {{
        document.querySelectorAll("[data-ars-protected-access-button]").forEach((button) => {{
          button.addEventListener("click", openDialog);
        }});

        const closeButton = document.querySelector("[data-ars-protected-access-close]");
        if (closeButton) {{
          closeButton.addEventListener("click", () => {{
            const dialog = document.getElementById("ars-protected-access-dialog");
            if (dialog && typeof dialog.close === "function") {{
              dialog.close();
            }}
          }});
        }}

        const form = document.getElementById("ars-protected-access-form");
        if (form) {{
          form.addEventListener("submit", (event) => {{
            event.preventDefault();
            const passwordInput = document.getElementById("ars-protected-access-password");
            unlockWithPassword(passwordInput ? passwordInput.value : "");
          }});
        }}

        const savedPassword = getSavedPassword();
        if (!savedPassword || !window.crypto || !crypto.subtle) {{
          setUnlocked(false);
          return;
        }}

        verifyPassword(savedPassword)
          .then((isValid) => {{
            if (isValid) {{
              setUnlocked(true);
            }} else {{
              forgetPassword();
              setUnlocked(false);
            }}
          }})
          .catch(() => {{
            forgetPassword();
            setUnlocked(false);
          }});
      }});
    }})();
  </script>"""


def render_protected_page(payload: dict[str, str | int]) -> str:
    payload_json = json.dumps(payload, ensure_ascii=False, separators=(",", ":"))
    return f"""<!DOCTYPE html>
<html lang="it">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  {PROTECTED_PAGE_MARKER}
  <title>Accesso riservato</title>
  <style>
    :root {{
      color-scheme: light dark;
      font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      background: #f5f7fb;
      color: #172033;
    }}
    body {{
      min-height: 100vh;
      margin: 0;
      display: grid;
      place-items: center;
      background:
        linear-gradient(135deg, rgba(26, 77, 136, 0.08), transparent 42%),
        linear-gradient(315deg, rgba(204, 48, 48, 0.07), transparent 40%),
        #f5f7fb;
    }}
    main {{
      width: min(420px, calc(100vw - 32px));
      padding: 32px;
      border: 1px solid rgba(23, 32, 51, 0.12);
      border-radius: 8px;
      background: rgba(255, 255, 255, 0.92);
      box-shadow: 0 20px 60px rgba(20, 31, 54, 0.14);
    }}
    h1 {{
      margin: 0 0 10px;
      font-size: 1.45rem;
      line-height: 1.2;
    }}
    p {{
      margin: 0 0 22px;
      color: #536071;
      line-height: 1.45;
    }}
    label {{
      display: block;
      margin-bottom: 8px;
      font-size: 0.9rem;
      font-weight: 650;
    }}
    input {{
      box-sizing: border-box;
      width: 100%;
      min-height: 44px;
      padding: 10px 12px;
      border: 1px solid #b9c2cf;
      border-radius: 6px;
      font: inherit;
      background: #fff;
      color: #172033;
    }}
    button {{
      width: 100%;
      min-height: 44px;
      margin-top: 14px;
      border: 0;
      border-radius: 6px;
      background: #184f90;
      color: #fff;
      font: inherit;
      font-weight: 700;
      cursor: pointer;
    }}
    button:disabled {{
      cursor: wait;
      opacity: 0.65;
    }}
    #error {{
      min-height: 1.4em;
      margin-top: 12px;
      color: #b3261e;
      font-size: 0.92rem;
    }}
    @media (prefers-color-scheme: dark) {{
      :root {{
        background: #101622;
        color: #ecf2fb;
      }}
      body {{
        background:
          linear-gradient(135deg, rgba(73, 145, 210, 0.18), transparent 42%),
          linear-gradient(315deg, rgba(230, 87, 87, 0.13), transparent 40%),
          #101622;
      }}
      main {{
        border-color: rgba(236, 242, 251, 0.18);
        background: rgba(23, 32, 48, 0.94);
        box-shadow: 0 20px 60px rgba(0, 0, 0, 0.36);
      }}
      p {{
        color: #b8c4d4;
      }}
      input {{
        border-color: #526175;
        background: #111927;
        color: #ecf2fb;
      }}
    }}
  </style>
</head>
<body>
  <main>
    <h1>Accesso riservato</h1>
    <p>Inserisci la password per visualizzare questa pagina.</p>
    <form id="unlock-form">
      <label for="password">Password</label>
      <input id="password" type="password" autocomplete="current-password" autofocus required>
      <button id="unlock-button" type="submit">Sblocca</button>
      <div id="error" role="alert" aria-live="polite"></div>
    </form>
  </main>
  <script type="application/json" id="ars-protected-page-data">{payload_json}</script>
  <script>
    (() => {{
      "use strict";

      const payload = JSON.parse(document.getElementById("ars-protected-page-data").textContent);
      const form = document.getElementById("unlock-form");
      const passwordInput = document.getElementById("password");
      const unlockButton = document.getElementById("unlock-button");
      const errorBox = document.getElementById("error");
      const storageKey = "arsProtectedPagePassword";
      const encoder = new TextEncoder();
      const decoder = new TextDecoder();

      function setError(message) {{
        errorBox.textContent = message;
      }}

      function getSavedPassword() {{
        try {{
          return sessionStorage.getItem(storageKey);
        }} catch (_) {{
          return null;
        }}
      }}

      function savePassword(password) {{
        try {{
          sessionStorage.setItem(storageKey, password);
        }} catch (_) {{
        }}
      }}

      function forgetPassword() {{
        try {{
          sessionStorage.removeItem(storageKey);
        }} catch (_) {{
        }}
      }}

      function b64ToBytes(value) {{
        const binary = atob(value);
        const bytes = new Uint8Array(binary.length);
        for (let i = 0; i < binary.length; i += 1) {{
          bytes[i] = binary.charCodeAt(i);
        }}
        return bytes;
      }}

      async function deriveKey(password, salt) {{
        const passwordKey = await crypto.subtle.importKey(
          "raw",
          encoder.encode(password),
          "PBKDF2",
          false,
          ["deriveKey"]
        );
        return crypto.subtle.deriveKey(
          {{
            name: "PBKDF2",
            salt,
            iterations: payload.iterations,
            hash: "SHA-256"
          }},
          passwordKey,
          {{ name: "AES-GCM", length: 256 }},
          false,
          ["decrypt"]
        );
      }}

      async function unlock(password, rememberPassword) {{
        const salt = b64ToBytes(payload.salt);
        const iv = b64ToBytes(payload.iv);
        const ciphertext = b64ToBytes(payload.ciphertext);
        const key = await deriveKey(password, salt);
        const clearBytes = await crypto.subtle.decrypt({{ name: "AES-GCM", iv }}, key, ciphertext);
        if (rememberPassword) {{
          savePassword(password);
        }}
        document.open();
        document.write(decoder.decode(clearBytes));
        document.close();
      }}

      if (!window.crypto || !crypto.subtle) {{
        unlockButton.disabled = true;
        setError("Apri la pagina tramite HTTPS o localhost per usare lo sblocco.");
        return;
      }}

      form.addEventListener("submit", async (event) => {{
        event.preventDefault();
        const password = passwordInput.value;
        unlockButton.disabled = true;
        setError("");
        try {{
          await unlock(password, true);
        }} catch (_) {{
          forgetPassword();
          unlockButton.disabled = false;
          passwordInput.select();
          setError("Password non valida.");
        }}
      }});

      const savedPassword = getSavedPassword();
      if (savedPassword) {{
        unlock(savedPassword, false).catch(() => forgetPassword());
      }}
    }})();
  </script>
</body>
</html>
"""


def resolve_href_to_site_relative(html_file: Path, site_root: Path, href: str) -> str | None:
    parsed = urlsplit(href)
    if parsed.scheme or parsed.netloc or parsed.path == "" or href.startswith("#"):
        return None
    if parsed.scheme in {"mailto", "tel", "javascript", "data"}:
        return None

    resolved_root = site_root.resolve()
    if parsed.path.startswith("/"):
        candidate = (resolved_root / unquote(parsed.path).lstrip("/")).resolve()
    else:
        candidate = (html_file.parent / Path(*PurePosixPath(unquote(parsed.path)).parts)).resolve()

    try:
        return candidate.relative_to(resolved_root).as_posix()
    except ValueError:
        return None


def annotate_protected_links(html: str, html_file: Path, site_root: Path, protected_paths: set[str]) -> str:
    def replace_anchor(match: re.Match[str]) -> str:
        attrs = match.group("attrs")
        if "data-ars-protected-link=" in attrs:
            return match.group(0)

        href = match.group("href")
        resolved_href = resolve_href_to_site_relative(html_file, site_root, href)
        if resolved_href not in protected_paths:
            return match.group(0)

        return f'<a data-ars-protected-link="true"{attrs}>'

    updated = ANCHOR_RE.sub(replace_anchor, html)
    return PROTECTED_NAV_ITEM_RE.sub(
        r'<li data-ars-protected-link-wrapper="true"\g<attrs>>\3',
        updated,
    )


def remove_existing_global_unlock_ui(html: str) -> str:
    html = GLOBAL_UNLOCK_STYLE_RE.sub("", html)
    html = GLOBAL_UNLOCK_SCRIPT_RE.sub("", html)
    html = GLOBAL_UNLOCK_DIALOG_RE.sub("", html)
    return GLOBAL_UNLOCK_BUTTON_RE.sub("", html)


def inject_global_unlock_ui(
    html_file: Path,
    site_root: Path,
    protected_paths: set[str],
    verifier_payload: dict[str, str | int],
) -> bool:
    html = html_file.read_text(encoding="utf-8")
    if PROTECTED_PAGE_MARKER in html:
        return False

    updated = remove_existing_global_unlock_ui(html)
    updated = annotate_protected_links(updated, html_file, site_root, protected_paths)

    style = render_global_unlock_style()
    if "</head>" in updated:
        updated = updated.replace("</head>", f"{style}\n  </head>", 1)

    button = render_global_unlock_button()
    updated = re.sub(
        r'(<div class="article-header-buttons">\s*)',
        r"\1" + button,
        updated,
        count=1,
    )

    dialog = render_global_unlock_dialog()
    script = render_global_unlock_script(verifier_payload)
    if "</body>" in updated:
        updated = updated.replace("</body>", f"{dialog}\n{script}\n</body>", 1)

    if updated == html:
        return False

    html_file.write_text(updated, encoding="utf-8")
    return True


def protect_html_file(html_file: Path, password: str) -> bool:
    html = html_file.read_text(encoding="utf-8")
    if PROTECTED_PAGE_MARKER in html:
        return False

    protected_html = render_protected_page(encrypt_html(html, password))
    html_file.write_text(protected_html, encoding="utf-8")
    return True


def _remap_doc_reference(value, doc_index_map: dict[int, int]):
    if isinstance(value, int):
        return doc_index_map.get(value)
    if isinstance(value, list):
        remapped = [doc_index_map[item] for item in value if isinstance(item, int) and item in doc_index_map]
        return remapped or None
    return value


def _prune_term_mapping(mapping: dict[str, object], doc_index_map: dict[int, int]) -> dict[str, object]:
    pruned: dict[str, object] = {}
    for term, value in mapping.items():
        remapped = _remap_doc_reference(value, doc_index_map)
        if remapped is not None:
            pruned[term] = remapped
    return pruned


def _prune_alltitles(mapping: dict[str, object], doc_index_map: dict[int, int]) -> dict[str, object]:
    pruned: dict[str, object] = {}
    for title, entries in mapping.items():
        if not isinstance(entries, list):
            continue
        updated_entries = []
        for entry in entries:
            if not isinstance(entry, list) or not entry:
                continue
            old_doc_index = entry[0]
            if not isinstance(old_doc_index, int) or old_doc_index not in doc_index_map:
                continue
            updated_entries.append([doc_index_map[old_doc_index], *entry[1:]])
        if updated_entries:
            pruned[title] = updated_entries
    return pruned


def prune_search_index(language_root: Path, protected_docnames: set[str]) -> bool:
    search_index = language_root / "searchindex.js"
    if not protected_docnames or not search_index.exists():
        return False

    content = search_index.read_text(encoding="utf-8")
    match = SEARCH_INDEX_RE.match(content)
    if not match:
        return False

    index = json.loads(match.group("payload"))
    docnames = index.get("docnames")
    if not isinstance(docnames, list):
        return False

    protected_indices = {i for i, docname in enumerate(docnames) if docname in protected_docnames}
    if not protected_indices:
        return False

    doc_index_map = {}
    next_index = 0
    for old_index in range(len(docnames)):
        if old_index in protected_indices:
            continue
        doc_index_map[old_index] = next_index
        next_index += 1

    for key in ("docnames", "filenames", "titles"):
        values = index.get(key)
        if isinstance(values, list):
            index[key] = [value for i, value in enumerate(values) if i not in protected_indices]

    for key in ("terms", "titleterms"):
        values = index.get(key)
        if isinstance(values, dict):
            index[key] = _prune_term_mapping(values, doc_index_map)

    alltitles = index.get("alltitles")
    if isinstance(alltitles, dict):
        index["alltitles"] = _prune_alltitles(alltitles, doc_index_map)

    updated = "Search.setIndex(" + json.dumps(index, ensure_ascii=False, separators=(",", ":")) + ")"
    search_index.write_text(updated, encoding="utf-8")
    return True


def protect_selected_pages(site_root: Path, page_specs: list[str], password: str | None = None) -> int:
    resolved_password = password if password is not None else get_protected_page_password()
    selected_pages = find_selected_pages(site_root, page_specs)
    protected_docnames_by_language: dict[Path, set[str]] = defaultdict(set)
    protected_count = 0
    protected_paths = {
        page.html_file.resolve().relative_to(site_root.resolve()).as_posix()
        for page in selected_pages
    }
    verifier_payload = encrypt_html(UNLOCK_VERIFIER_TEXT, resolved_password)

    if protected_paths:
        for html_file in sorted(site_root.rglob("*.html")):
            inject_global_unlock_ui(html_file, site_root, protected_paths, verifier_payload)

    for page in selected_pages:
        protected_docnames_by_language[page.language_root].add(page.docname)
        if protect_html_file(page.html_file, resolved_password):
            protected_count += 1

    for language_root, protected_docnames in protected_docnames_by_language.items():
        prune_search_index(language_root, protected_docnames)

    return protected_count
