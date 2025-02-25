import logging
import os

from from_root import from_root
from datetime import datetime

# Log constants
LOGS_DIR = 'logs'
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"


# Directory structure based on category
logs_path = os.path.join(from_root(), LOGS_DIR, LOG_FILE)
print(f"Log file will be written to: {logs_path}")  # Debug statement
os.makedirs(LOGS_DIR, exist_ok=True)


logging.basicConfig(
    filename=logs_path,
    format="[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
    level=logging.DEBUG,
)