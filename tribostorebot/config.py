import configparser
import os

from definitions import CONFIG_FILEPATH

class Config():

    def __init__(self):
        self.token = self._get_bot_token()

        config = self._read_config_file()
        self.fetch_interval = config['BOT'].getint('fetch_interval_seconds')
        self.request_url = config['SCRAPER'].get('request_url')

    def _read_config_file(self):
        config = configparser.ConfigParser()
        config.read(CONFIG_FILEPATH)
        return config

    def _get_bot_token(self):
        return os.environ['TRIBOSTOREBOT_TOKEN']
