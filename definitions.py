from pathlib import Path

CONFIG_FILEPATH = Path('.') / 'config' / 'config.ini'
LOG_PATH = Path('.') / 'log'
DATA_PATH = Path('.') / 'data'

if not LOG_PATH.exists():
    Path.mkdir(LOG_PATH)

if not DATA_PATH.exists():
    Path.mkdir(DATA_PATH)
