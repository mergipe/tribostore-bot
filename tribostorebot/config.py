import configparser
import os

from definitions import CONFIG_FILEPATH


class Config():

    def __init__(self):
        self.token = os.environ['TRIBOSTOREBOT_TOKEN']
        self.access_code = os.environ['TRIBOSTOREBOT_ACCESS_CODE']

        config = self._read_config_file()
        self.fetch_interval = config['BOT'].getint('fetch_interval_seconds')
        self.request_url = config['ITEM RETRIEVER'].get('request_url')

    def _read_config_file(self):
        config = configparser.ConfigParser()
        config.read(CONFIG_FILEPATH)
        return config
