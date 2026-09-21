"""Cap the pixel width of source images.

The FlexiBowl manual ships diagrams exported at print resolution — the largest
are 16837 x 11905 (200 MP, ~14 MB each) and are displayed in a roughly 1000 px
content column. Capping width at 2560 px keeps them crisp on retina displays
while cutting the repository by several hundred megabytes.

GIFs are deliberately excluded: they are animated here, and Pillow's resize
would flatten them to a single frame.
"""

from __future__ import annotations

import io
from pathlib import Path

from PIL import Image

# The source diagrams exceed Pillow's default 178 MP decompression-bomb limit.
# They are our own CAD exports, not untrusted input.
Image.MAX_IMAGE_PIXELS = None

MAX_IMAGE_WIDTH = 2560
CAPPED_SUFFIXES = frozenset({".png", ".jpg", ".jpeg"})


def cap_image_bytes(data: bytes, max_width: int = MAX_IMAGE_WIDTH) -> bytes | None:
    """Downscale image bytes to `max_width`, preserving aspect ratio.

    Returns None when the image is already at or below the cap, so callers can
    cheaply skip writing.
    """
    with Image.open(io.BytesIO(data)) as image:
        image_format = image.format
        if image_format not in {"PNG", "JPEG"}:
            return None

        width, height = image.size
        if width <= max_width:
            return None

        new_height = round(height * max_width / width)

        # Convert palette and 1-bit modes to RGBA so that LANCZOS filtering
        # actually applies. Pillow silently falls back to NEAREST for P and 1 modes.
        if image.mode in {"P", "1"}:
            image = image.convert("RGBA")

        resized = image.resize((max_width, new_height), Image.LANCZOS)

        save_kwargs: dict[str, object] = {"optimize": True}
        if image_format == "JPEG":
            save_kwargs["quality"] = 90
            if resized.mode not in {"RGB", "L"}:
                resized = resized.convert("RGB")

        buffer = io.BytesIO()
        resized.save(buffer, image_format, **save_kwargs)

    return buffer.getvalue()


def cap_image_file(path: Path, max_width: int = MAX_IMAGE_WIDTH) -> bool:
    """Downscale `path` in place. Returns True when the file was rewritten."""
    if path.suffix.lower() not in CAPPED_SUFFIXES:
        return False

    original = path.read_bytes()
    capped = cap_image_bytes(original, max_width)
    if capped is None:
        return False

    path.write_bytes(capped)
    return True


def cap_directory(root: Path, max_width: int = MAX_IMAGE_WIDTH) -> tuple[int, int]:
    """Cap every eligible image under `root`. Returns (files_changed, bytes_saved)."""
    files_changed = 0
    bytes_saved = 0

    for path in sorted(root.rglob("*")):
        if not path.is_file() or path.suffix.lower() not in CAPPED_SUFFIXES:
            continue

        before = path.stat().st_size
        if cap_image_file(path, max_width):
            files_changed += 1
            bytes_saved += before - path.stat().st_size

    return files_changed, bytes_saved
