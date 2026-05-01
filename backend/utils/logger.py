import logging
from loguru import logger as loguru_logger
import os

def get_logger(name, file_path):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    loguru_logger.add(file_path, rotation="10 MB", retention="10 days", level="INFO")
    return loguru_logger.bind(name=name)

def setup_logging():
    logging.basicConfig(level=logging.INFO)
    loguru_logger.add("logs/system_logs/system.log", rotation="10 MB", retention="10 days", level="INFO")
