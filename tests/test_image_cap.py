import io
from pathlib import Path

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


def test_width_invariant_enforced(tmp_path: Path):
    """Width cap is enforced unconditionally, even if re-encode isn't smaller.

    The width cap (MAX_IMAGE_WIDTH) is a binding constraint, not a size optimization.
    After cap_image_file returns True, the stored file must have width == MAX_IMAGE_WIDTH.
    """
    target = tmp_path / "wide.png"
    target.write_bytes(make_png(9000, 3000))
    assert cap_image_file(target) is True
    with Image.open(target) as im:
        assert im.size[0] == MAX_IMAGE_WIDTH, (
            f"Width not capped: got {im.size[0]}, expected {MAX_IMAGE_WIDTH}"
        )


def test_palette_images_are_really_antialiased():
    """Pillow forces NEAREST for mode "P" unless the image is promoted first.

    A flat-colour fixture would pass vacuously: every filter agrees on it.
    Built from linear_gradient (256x256) and scaled up: a putdata list at
    these dimensions would allocate gigabytes.
    """
    ramp = Image.linear_gradient("L")
    gradient = Image.merge("RGB", (
        ramp,
        ramp.transpose(Image.ROTATE_90),
        ramp.transpose(Image.ROTATE_180),
    ))
    buf = io.BytesIO()
    gradient.resize((3000, 750), Image.NEAREST).convert("P").save(buf, "PNG")

    capped = cap_image_bytes(buf.getvalue())
    assert capped is not None
    with Image.open(io.BytesIO(capped)) as got:
        antialiased = got.convert("RGB").tobytes()
        size = got.size
    with Image.open(io.BytesIO(buf.getvalue())) as src:
        nearest = src.resize(size, Image.NEAREST).convert("RGB").tobytes()
    assert antialiased != nearest
