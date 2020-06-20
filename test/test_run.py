import requests
import run
import sys

def test_logging_config(tmp_path):
    run.LOG_PATH = tmp_path
    run._config_logging()
    assert len(list(tmp_path.iterdir())) == 1

    log_filepath = list(tmp_path.iterdir())[0]
    with open(log_filepath, 'w') as logfile:
        assert sys.stdout.name == logfile.name
        assert sys.stderr.name == logfile.name

def test_config_file_entries():
    config = run._read_config_file()
    assert 'BOT' in config
    assert 'SCRAPER' in config
    assert 'fetch_interval_seconds' in config['BOT']
    assert 'request_url' in config['SCRAPER']

def test_config_file_data_types():
    config = run._read_config_file()
    assert config['BOT']['fetch_interval_seconds'].isdigit()
    try:
        resp = requests.get(config['SCRAPER']['request_url'])
        assert resp.ok
    except:
        pytest.fail("Invalid 'requests_url' field.")
