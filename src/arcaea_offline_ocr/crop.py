from typing import Any, Tuple

from .device import Device
from .types import Mat

__all__ = [
    "crop_img",
    "crop_from_device_attr",
    "crop_to_pure",
    "crop_to_far",
    "crop_to_lost",
    "crop_to_max_recall",
    "crop_to_rating_class",
    "crop_to_score",
    "crop_to_title",
]


def crop_img(img: Mat, *, top: int, left: int, bottom: int, right: int):
    return img[top:bottom, left:right]


def crop_from_device_attr(img: Mat, rect: Tuple[int, int, int, int]):
    x, y, w, h = rect
    return crop_img(img, top=y, left=x, bottom=y + h, right=x + w)


def crop_to_pure(screenshot: Mat, device: Device):
    return crop_from_device_attr(screenshot, device.pure)


def crop_to_far(screenshot: Mat, device: Device):
    return crop_from_device_attr(screenshot, device.far)


def crop_to_lost(screenshot: Mat, device: Device):
    return crop_from_device_attr(screenshot, device.lost)


def crop_to_max_recall(screenshot: Mat, device: Device):
    return crop_from_device_attr(screenshot, device.max_recall)


def crop_to_rating_class(screenshot: Mat, device: Device):
    return crop_from_device_attr(screenshot, device.rating_class)


def crop_to_score(screenshot: Mat, device: Device):
    return crop_from_device_attr(screenshot, device.score)


def crop_to_title(screenshot: Mat, device: Device):
    return crop_from_device_attr(screenshot, device.title)
