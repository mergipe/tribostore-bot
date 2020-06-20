from pathlib import Path

def create_directories():
    if not LOG_PATH.exists():
        Path.mkdir(LOG_PATH)

    if not DATA_PATH.exists():
        Path.mkdir(DATA_PATH)

CONFIG_FILEPATH = Path('.') / 'config' / 'config.ini'
LOG_PATH = Path('.') / 'log'
DATA_PATH = Path('.') / 'data'

create_directories()
