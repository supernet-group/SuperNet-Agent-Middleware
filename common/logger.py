import logging
import sys
from pathlib import Path
from logging.handlers import RotatingFileHandler
from common.config import static_config, dynamic_config

# log format
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True) 
LOG_FILE = LOG_DIR / "supernet-agent-middleware.log"

def setup_logger():
    log_level = logging.DEBUG if dynamic_config.DEBUG_MODE else logging.INFO

    logger = logging.getLogger()
    logger.setLevel(log_level)

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(logging.Formatter(LOG_FORMAT))
    logger.addHandler(console_handler)

    file_handler = RotatingFileHandler(
        LOG_FILE, maxBytes=10 * 1024 * 1024, backupCount=5  # 10MB per file, keep 5 backups
    )
    file_handler.setFormatter(logging.Formatter(LOG_FORMAT))
    logger.addHandler(file_handler)

    return logger

logger = setup_logger()