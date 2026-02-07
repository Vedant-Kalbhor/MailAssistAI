import logging
from config import Config

logging.basicConfig(
    filename=Config.LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

def log(message):
    logging.info(message)
