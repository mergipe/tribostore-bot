import definitions

def test_data_path():
    assert definitions.DATA_PATH.exists()
    assert definitions.DATA_PATH.is_dir()

def test_log_path():
    assert definitions.LOG_PATH.exists()
    assert definitions.LOG_PATH.is_dir()

def test_config_filepath():
    assert definitions.CONFIG_FILEPATH.exists()
    assert definitions.CONFIG_FILEPATH.is_file()
