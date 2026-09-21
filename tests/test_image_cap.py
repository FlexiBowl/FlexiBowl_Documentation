import io
from pathlib import Path

import pytest
from PIL import Image

from tools.manual_publisher.image_cap import (
    MAX_IMAGE_WIDTH,
    cap_directory,
    cap_image_bytes,
    cap_image_file,
)


def make_png(width: int, height: int, colour=(120, 30, 200)) -> bytes:
    buf = io.BytesIO()
    Image.new("RGB", (width, height), colour).save(buf, "PNG")
    return buf.getvalue()


def test_returns_none_when_already_narrow_enough():
    assert cap_image_bytes(make_png(800, 600)) is None


def test_returns_none_at_exactly_the_cap():
    assert cap_image_bytes(make_png(MAX_IMAGE_WIDTH, 1000)) is None


def test_downscales_wide_image_to_cap():
    out = cap_image_bytes(make_png(16837, 11905))
    assert out is not None
    with Image.open(io.BytesIO(out)) as im:
        assert im.size == (2560, 1810)


def test_preserves_aspect_ratio():
    out = cap_image_bytes(make_png(8000, 2000))
    with Image.open(io.BytesIO(out)) as im:
        width, height = im.size
    assert width == 2560
    assert height == round(2000 * 2560 / 8000)


def test_identical_inputs_give_identical_dimensions():
    # The component-overlay widget stacks 14 images absolutely; they must stay
    # mutually dimension-identical or the highlights misalign.
    a = cap_image_bytes(make_png(16837, 11905, (10, 20, 30)))
    b = cap_image_bytes(make_png(16837, 11905, (200, 180, 160)))
    with Image.open(io.BytesIO(a)) as ia, Image.open(io.BytesIO(b)) as ib:
        assert ia.size == ib.size


def test_preserves_format():
    buf = io.BytesIO()
    Image.new("RGB", (6000, 4000), (1, 2, 3)).save(buf, "JPEG")
    out = cap_image_bytes(buf.getvalue())
    with Image.open(io.BytesIO(out)) as im:
        assert im.format == "JPEG"


def test_actually_shrinks_the_payload():
    src = make_png(16837, 11905)
    out = cap_image_bytes(src)
    assert len(out) < len(src)


def test_cap_image_file_rewrites_in_place(tmp_path: Path):
    target = tmp_path / "big.png"
    target.write_bytes(make_png(5000, 2500))
    assert cap_image_file(target) is True
    with Image.open(target) as im:
        assert im.size[0] == 2560
    assert cap_image_file(target) is False  # idempotent


def test_cap_directory_skips_gif(tmp_path: Path):
    gif = tmp_path / "anim.gif"
    Image.new("P", (4000, 3000)).save(gif, "GIF")
    before = gif.read_bytes()
    changed, _ = cap_directory(tmp_path)
    assert changed == 0
    assert gif.read_bytes() == before


def test_cap_directory_reports_savings(tmp_path: Path):
    (tmp_path / "a.png").write_bytes(make_png(6000, 3000))
    (tmp_path / "sub").mkdir()
    (tmp_path / "sub" / "b.png").write_bytes(make_png(7000, 3500))
    (tmp_path / "small.png").write_bytes(make_png(100, 100))
    changed, saved = cap_directory(tmp_path)
    assert changed == 2
    assert saved > 0
