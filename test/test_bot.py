from tribostorebot.bot import TriboStoreBot
from tribostorebot.items import ItemRetriever


def test_bot_instantiation():
    token = 'test_token'
    fetch_interval = 60
    request_url = 'test_url'
    b = TriboStoreBot(token, request_url, fetch_interval)
    assert b.token == token
    assert b.fetch_interval == fetch_interval
    assert isinstance(b.retriever, ItemRetriever)
