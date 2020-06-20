import run
import sys

def test_logging_setup(tmp_path):
    run.LOG_PATH = tmp_path
    run._setup_logging()
    assert len(list(tmp_path.iterdir())) == 1

    log_filepath = list(tmp_path.iterdir())[0]
    with open(log_filepath, 'w') as logfile:
        assert sys.stdout.name == logfile.name
        assert sys.stderr.name == logfile.name
