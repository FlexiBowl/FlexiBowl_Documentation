from pathlib import Path

import pytest

from tools.ci.rewrite_cdn_urls import (
    is_offloaded,
    resolve_to_build_relative,
    rewrite_html,
    rewrite_tree,
)

CDN = "https://d111111abcdef8.cloudfront.net"
BUILD = Path("build")


@pytest.mark.parametrize(
    "rel,expected",
    [
        ("_shared/static/theme.css", True),
        ("_assets/logo.png", True),
        ("V. 1.0/IT/_images/a.mp4", True),
        ("V. 1.0/EN/_downloads/doc.pdf", True),
        ("V. 1.0/IT/index.html", False),
        ("index.html", False),
        ("V. 1.0/IT/FlexiBowl_manual/page.html", False),
    ],
)
def test_is_offloaded(rel, expected):
    assert is_offloaded(rel) is expected


def test_resolve_walks_up_from_nested_page():
    page = BUILD / "V. 1.0/IT/FlexiBowl_manual/INSTALLAZIONE/p.html"
    assert resolve_to_build_relative(page, BUILD, "../../_images/a.mp4") == "V. 1.0/IT/_images/a.mp4"


def test_resolve_handles_bare_reference_from_language_index():
    page = BUILD / "V. 1.0/IT/index.html"
    assert resolve_to_build_relative(page, BUILD, "_images/x.png") == "V. 1.0/IT/_images/x.png"


def test_resolve_decodes_percent_encoding():
    page = BUILD / "index.html"
    assert resolve_to_build_relative(page, BUILD, "./V.%201.0/IT/_images/a.png") == "V. 1.0/IT/_images/a.png"


@pytest.mark.parametrize(
    "url",
    ["https://example.com/a.png", "//cdn.example.com/a.png", "/absolute.png",
     "#anchor", "data:image/png;base64,AAA", "mailto:a@b.c"],
)
def test_resolve_rejects_non_relative(url):
    assert resolve_to_build_relative(BUILD / "index.html", BUILD, url) is None


def test_resolve_rejects_escape_above_build_root():
    assert resolve_to_build_relative(BUILD / "index.html", BUILD, "../../etc/passwd") is None


def test_rewrite_shared_asset_with_query_string():
    page = BUILD / "V. 1.0/IT/index.html"
    html = '<link href="../../_shared/static/theme.css?digest=abc123" rel="stylesheet">'
    out = rewrite_html(html, page, BUILD, CDN)
    assert out == f'<link href="{CDN}/_shared/static/theme.css?digest=abc123" rel="stylesheet">'


def test_rewrite_encodes_spaces_in_version_directory():
    page = BUILD / "V. 1.0/IT/FlexiBowl_manual/X/p.html"
    html = '<video src="../../_images/installazione_FB800.mp4"></video>'
    out = rewrite_html(html, page, BUILD, CDN)
    assert out == f'<video src="{CDN}/V.%201.0/IT/_images/installazione_FB800.mp4"></video>'


def test_rewrite_leaves_internal_links_alone():
    page = BUILD / "V. 1.0/IT/index.html"
    html = '<a href="FlexiBowl_manual/intro.html">Intro</a>'
    assert rewrite_html(html, page, BUILD, CDN) == html


def test_rewrite_preserves_fragment():
    page = BUILD / "V. 1.0/IT/index.html"
    html = '<a href="../../_downloads/doc.pdf#page=3">Doc</a>'
    out = rewrite_html(html, page, BUILD, CDN)
    assert out == f'<a href="{CDN}/_downloads/doc.pdf#page=3">Doc</a>'


def test_rewrite_ignores_script_bodies():
    page = BUILD / "V. 1.0/IT/index.html"
    html = '<script>var s = \'src="_images/fake.png"\';</script>'
    assert rewrite_html(html, page, BUILD, CDN) == html


def test_rewrite_handles_single_quoted_attributes():
    page = BUILD / "V. 1.0/IT/index.html"
    html = "<img src='_images/a.png'>"
    out = rewrite_html(html, page, BUILD, CDN)
    assert out == f"<img src='{CDN}/V.%201.0/IT/_images/a.png'>"


def test_rewrite_is_idempotent():
    page = BUILD / "V. 1.0/IT/index.html"
    html = '<img src="_images/a.png">'
    once = rewrite_html(html, page, BUILD, CDN)
    assert rewrite_html(once, page, BUILD, CDN) == once


def test_rewrite_tree_walks_html_files(tmp_path: Path):
    build = tmp_path / "build"
    (build / "V. 1.0" / "IT").mkdir(parents=True)
    (build / "V. 1.0" / "IT" / "index.html").write_text('<img src="_images/a.png">', encoding="utf-8")
    (build / "V. 1.0" / "IT" / "notes.txt").write_text('<img src="_images/a.png">', encoding="utf-8")
    files_changed, urls_rewritten = rewrite_tree(build, CDN)
    assert (files_changed, urls_rewritten) == (1, 1)
    assert CDN in (build / "V. 1.0" / "IT" / "index.html").read_text(encoding="utf-8")
    assert CDN not in (build / "V. 1.0" / "IT" / "notes.txt").read_text(encoding="utf-8")
