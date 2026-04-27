import logging
import os

def setup_logger():
    os.makedirs("logs",exist_ok= True)

    logging.basicConfig(
        level=logging.INFO,
        format = "%(asctime)s - %(levelname)s - %(message)s",
        filename="logs/app.log",
        force=True
    )

    # print logs to console
    logging.getLogger().addHandler(logging.StreamHandler())

