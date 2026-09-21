"""Rewrite relative asset URLs in built HTML to absolute CDN URLs.

Runs in CI only. The HTML committed to the repository keeps its original
relative paths so that opening `build/index.html` locally still works offline.

Unlike FlexiVision, this manual emits per-language `_images/` and `_downloads/`
directories whose references are relative to each HTML file's own location, so
every URL has to be resolved against its containing file rather than matched by
a fixed pattern.
"""

from __future__ import annotations

import argparse
import posixpath
import re
import sys
from pathlib import Path
from urllib.parse import quote, unquote

OFFLOAD_PREFIXES = ("_shared/", "_assets/")
OFFLOAD_DIR_NAMES = frozenset({"_images", "_downloads"})

_ATTR_RE = re.compile(r"""\b(src|href|poster)=(["'])([^"']*)\2""")
_NON_RELATIVE_PREFIXES = ("http://", "https://", "//", "/", "#", "data:", "mailto:", "javascript:", "tel:")


def is_offloaded(rel_posix: str) -> bool:
    """True when a build-root-relative path belongs on the CDN."""
    if rel_posix.startswith(OFFLOAD_PREFIXES):
        return True
    return any(segment in OFFLOAD_DIR_NAMES for segment in rel_posix.split("/")[:-1])


def _split_url(url: str) -> tuple[str, str]:
    """Split a URL into (path, suffix) where suffix keeps any ?query or #fragment.

    Splits at whichever marker appears first: Sphinx emits both forms, and
    "a.css?v=1#f" must not put "?v=1" into the path, where it would be
    percent-encoded into the CDN URL.
    """
    indices = [i for i in (url.find("?"), url.find("#")) if i != -1]
    if not indices:
        return url, ""
    cut = min(indices)
    return url[:cut], url[cut:]


def resolve_to_build_relative(html_path: Path, build_root: Path, url: str) -> str | None:
    """Resolve a relative URL against its HTML file, returning a build-root-relative path.

    Returns None for absolute, external or non-path URLs, and for anything that
    escapes the build root.
    """
    if not url or url.startswith(_NON_RELATIVE_PREFIXES):
        return None

    path_part, _ = _split_url(url)
    if not path_part:
        return None

    html_dir = html_path.parent.as_posix()
    build_dir = build_root.as_posix()
    absolute = posixpath.normpath(posixpath.join(html_dir, unquote(path_part)))

    prefix = build_dir + "/"
    if not absolute.startswith(prefix):
        return None

    return absolute[len(prefix):]


def rewrite_html(text: str, html_path: Path, build_root: Path, cdn_base: str) -> str:
    """Rewrite offloaded asset URLs in one HTML document."""
    base = cdn_base.rstrip("/")

    def replace_attr(match: re.Match[str]) -> str:
        attribute, quote_char, url = match.group(1), match.group(2), match.group(3)
        relative = resolve_to_build_relative(html_path, build_root, url)
        if relative is None or not is_offloaded(relative):
            return match.group(0)
        _, suffix = _split_url(url)
        encoded = quote(relative, safe="/")
        return f"{attribute}={quote_char}{base}/{encoded}{suffix}{quote_char}"

    # Script bodies are rewritten too. The theme emits its dark-mode logo with
    # document.write(`<img src="../../_shared/...">`), so skipping <script> would
    # leave that image pointing at the docs origin, where nginx returns 404. The
    # real guard is is_offloaded(): a string is only touched when it resolves to
    # a path we actually host on the CDN.
    return _ATTR_RE.sub(replace_attr, text)


def rewrite_tree(build_root: Path, cdn_base: str) -> tuple[int, int]:
    """Rewrite every .html file under build_root. Returns (files_changed, urls_rewritten)."""
    files_changed = 0
    urls_rewritten = 0

    for html_path in sorted(build_root.rglob("*.html")):
        original = html_path.read_text(encoding="utf-8", errors="surrogateescape")
        updated = rewrite_html(original, html_path, build_root, cdn_base)
        if updated == original:
            continue
        urls_rewritten += updated.count(cdn_base.rstrip("/")) - original.count(cdn_base.rstrip("/"))
        html_path.write_text(updated, encoding="utf-8", errors="surrogateescape")
        files_changed += 1

    return files_changed, urls_rewritten


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Rewrite built HTML asset URLs to a CDN base.")
    parser.add_argument("--build-root", type=Path, default=Path("build"))
    parser.add_argument("--cdn-base", required=True)
    args = parser.parse_args(argv)

    if not args.cdn_base.startswith(("http://", "https://")):
        print(f"::error::CDN base must start with http:// or https:// (got: {args.cdn_base})", file=sys.stderr)
        return 1
    if not args.build_root.is_dir():
        print(f"::error::build root not found: {args.build_root}", file=sys.stderr)
        return 1

    files_changed, urls_rewritten = rewrite_tree(args.build_root, args.cdn_base)
    print(f"rewrote {urls_rewritten} URLs across {files_changed} HTML files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
