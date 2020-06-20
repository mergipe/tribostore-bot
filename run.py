import logging
import sys
from datetime import datetime

from definitions import LOG_PATH

def _config_logging():
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
    _config_logging()

if __name__ == '__main__':
    main()
