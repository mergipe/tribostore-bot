import requests
import pytest

from tribostorebot.config import Config

def test_config_url():
    cfg = Config()
    resp = requests.get(cfg.request_url)
    assert resp.ok
