from io import BytesIO
from typing import Optional, Union

from PIL import Image

from nidhoggr.errors.texture import UnsupportedFormat, UnsupportedSize

AVAILABLE_SIZES = frozenset({64, 128, 256, 512, 1024})


def check_texture(*, data: bytes) -> Optional[Union[UnsupportedFormat, UnsupportedSize]]:
    with Image.open(BytesIO(data)) as image:
        if image.format != "PNG":
            return UnsupportedFormat
        (width, height) = image.size
        valid = width / 2 == height or width == height
        if not valid or width not in AVAILABLE_SIZES:
            return UnsupportedSize


def optimize_texture(*, data: bytes) -> bytes:
    return data
