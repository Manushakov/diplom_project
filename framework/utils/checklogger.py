import logging
from singleton import Singleton


class CheckLogger(metaclass=Singleton):
    __logger = None

    def __init__(self):
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)
        logger_handler = logging.FileHandler("program.log")
        logger_handler.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        logger_handler.setFormatter(formatter)
        logger.addHandler(logger_handler)
        CheckLogger.__logger = logger

    @staticmethod
    def info(message, name=""):
        CheckLogger.__logger.info(message + " - " + name)

    @staticmethod
    def warning(message):
        CheckLogger.__logger.warning(msg=message)

    @staticmethod
    def error(message):
        CheckLogger.__logger.error(msg=message)

    @staticmethod
    def fatal(message):
        CheckLogger.__logger.fatal(msg=message)
