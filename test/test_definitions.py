import definitions

def _assert_data_path():
    assert definitions.DATA_PATH.exists()
    assert definitions.DATA_PATH.is_dir()

def _assert_log_path():
    assert definitions.LOG_PATH.exists()
    assert definitions.LOG_PATH.is_dir()

def _remove_data_dir():
    if definitions.DATA_PATH.exists():
        definitions.DATA_PATH.rmdir()

def _remove_log_dir():
    if definitions.LOG_PATH.exists():
        definitions.LOG_PATH.rmdir()

def test_if_config_filepath_is_correct():
    assert definitions.CONFIG_FILEPATH.exists()
    assert definitions.CONFIG_FILEPATH.is_file()

def test_if_data_and_log_paths_are_correctly_created():
    _remove_data_dir()
    _remove_log_dir()
    definitions.create_directories()
    _assert_data_path()
    _assert_log_path()

def test_if_data_and_log_paths_are_correct():
    definitions.create_directories()
    _assert_data_path()
    _assert_log_path()
