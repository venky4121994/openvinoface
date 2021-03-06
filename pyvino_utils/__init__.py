# -*- coding: utf-8 -*-

"""Top-level package for pyvino-utils."""

__author__ = """Mpho Mphego"""
__email__ = "mpho@mphomphego.co.za"


# Python standard library
import os
import pkgutil

from pyvino_utils import __version__, __vino_version__
from pyvino_utils.input_handler.input_feeder import InputFeeder
from pyvino_utils.opencv_utils import cv_utils
try:
    from pyvino_utils.models import detection, openvino_base, pose_estimations, recognition
except ModuleNotFoundError:
    from loguru import logger
    logger.warning("OpenVINO is not installed, your mileage may vary!")

__version__ = __version__.__version__
__vino_version__ = __vino_version__.__vino_version__

# Automatically load all modules from current dir
__all__ = [module for _, module, _ in pkgutil.iter_modules([os.path.dirname(__file__)])]
