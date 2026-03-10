import logging
import os

log_folder = "logs"

if not os.path.exists(log_folder):
    os.makedirs(log_folder)

logging.basicConfig(
    filename="logs/app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def get_logger():
    return logging.getLogger()