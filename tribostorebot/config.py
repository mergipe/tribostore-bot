import configparser
import os

from definitions import CONFIG_FILEPATH


class Config():

    def __init__(self):
        self.token = os.environ['TRIBOSTOREBOT_TOKEN']
        self.access_code = os.environ['TRIBOSTOREBOT_ACCESS_CODE']

        cfg = self._read_config_file()
        self.retrieve_interval = cfg['BOT'].getint('retrieve_interval_seconds')
        self.request_url = cfg['ITEM RETRIEVER'].get('request_url')

    def _read_config_file(self):
        cfg = configparser.ConfigParser()
        cfg.read(CONFIG_FILEPATH)
        return cfg
