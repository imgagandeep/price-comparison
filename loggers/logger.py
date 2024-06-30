# Standard library imports
import sys
import logging
from typing import NoReturn

# Get an instance of a logger
logger = logging.getLogger(__name__)

# Now we are going to Set the threshold of logger to DEBUG
logger.setLevel(logging.DEBUG)

# define file name and log format
logging.basicConfig(
    datefmt="%Y-%m-%d %H:%M:%S",
    filemode="a",
    filename="config.log",
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s - %(pathname)s - %(lineno)d - %(funcName)s",
)


def critical(message: str) -> NoReturn:
    """
    Logs a critical message.
    """
    exc_type, exc_obj, exc_tb = sys.exc_info()
    logger.critical(message, exc_info=(exc_type, exc_obj, exc_tb))


def debug(message: str) -> NoReturn:
    """
    Logs a debug message.
    """
    logger.debug(message)


def error(message: str) -> NoReturn:
    """
    Logs an error message.
    """
    exc_type, exc_obj, exc_tb = sys.exc_info()
    logger.error(message, exc_info=(exc_type, exc_obj, exc_tb))


def exception(message: str) -> NoReturn:
    """
    Logs an exception message.
    """
    exc_type, exc_obj, exc_tb = sys.exc_info()
    logger.exception(message, exc_info=(exc_type, exc_obj, exc_tb))


def info(message: str) -> NoReturn:
    """
    Logs an info message.
    """
    logger.info(message)


def warning(message: str) -> NoReturn:
    """
    Logs a warning message.
    """
    exc_type, exc_obj, exc_tb = sys.exc_info()
    logger.warning(message, exc_info=(exc_type, exc_obj, exc_tb))
