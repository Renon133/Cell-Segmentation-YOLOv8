from cell_segmentation.logger import logging
from cell_segmentation.exception import AppException
import sys

try:
    # Application logic goes here
    logging.info("Application is running successfully.")
    a = 2/0  # This will raise an exception
except Exception as e:
    raise AppException(e, sys)