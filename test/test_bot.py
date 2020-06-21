from tribostorebot.bot import TriboStoreBot
from tribostorebot.items import ItemRetriever


def test_bot_instantiation():
    token = 'test_token'
    retrieve_interval = 60
    request_url = 'test_url'
    b = TriboStoreBot(token, request_url, retrieve_interval)
    assert b.token == token
    assert b.retrieve_interval == retrieve_interval
    assert isinstance(b.retriever, ItemRetriever)
