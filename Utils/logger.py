import logging
import os
from datetime import datetime
from Utils.config_reader import LEVEL

# ---------- globals ----------
LOG_CREATED = False
LOG_FILE_PATH = None

# ---------- project root ----------
PROJECT_ROOT = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)


def _create_log_file():
    global LOG_CREATED, LOG_FILE_PATH

    if not LOG_CREATED:
        # create logs folder at PROJECT ROOT (not test folder)
        log_dir = os.path.join(PROJECT_ROOT, "logs")
        os.makedirs(log_dir, exist_ok=True)

        timestamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")

        LOG_FILE_PATH = os.path.join(
            log_dir,
            f"execution_{timestamp}.log"
        )

        LOG_CREATED = True

    return LOG_FILE_PATH


def get_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)

    # ---------- level ----------
    level = getattr(logging, LEVEL.upper(), logging.INFO)
    logger.setLevel(level)

    # ---------- prevent duplicate handlers ----------
    if logger.handlers:
        return logger

    log_file = _create_log_file()

    # ---------- handlers ----------
    file_handler = logging.FileHandler(log_file, encoding="utf-8")
    console_handler = logging.StreamHandler()

    # ---------- formatter ----------
    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s"
    )

    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger


# test
logger = get_logger("test")
logger.info("Logger initialized")
