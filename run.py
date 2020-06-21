import logging
import sys
from datetime import datetime

from definitions import LOG_PATH
from tribostorebot.bot import TriboStoreBot
from tribostorebot.config import Config

def _setup_logging():
    log_filename = datetime.now().strftime('%d_%m_%Y_%H_%M_%S') + '.log'
    log_filepath = LOG_PATH / log_filename

    logging.basicConfig(
        filename=log_filepath,
        format='[%(asctime)s] %(levelname)s: %(message)s',
        datefmt='%d/%m/%Y %H:%M:%S',
        level=logging.INFO
    )

    log_file = open(log_filepath, 'w')
    sys.stdout = log_file
    sys.stderr = log_file

def main():
    _setup_logging()
    cfg = Config()
    bot = TriboStoreBot(cfg.token, cfg.request_url, cfg.retrieve_interval)
    bot.start()

if __name__ == '__main__':
    main()
