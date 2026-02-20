import logging
import os

LOG_FILE=os.path.join(os.getcwd(), "bot.log")

def setup_logger():
    logger=logging.getLogger("BinanceBot")
    logger.setLevel(logging.DEBUG)

    if not logger.handlers:
        file_handler = logging.FileHandler(LOG_FILE) 
        file_handler.setLevel(logging.DEBUG)

        formatter=logging.Formatter("%(asctime)s | %(levelname)s | %(name)s | %(message)s")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    return logger
logger=setup_logger()