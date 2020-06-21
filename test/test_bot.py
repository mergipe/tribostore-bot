from tribostorebot.bot import TriboStoreBot
from tribostorebot.items import ItemRetriever


def test_bot_instantiation():
    token = 'test_token'
    retrieve_interval = 60
    access_code = 'test_code'
    request_url = 'test_url'
    b = TriboStoreBot(token, access_code, request_url, retrieve_interval)

    assert b._token == token
    assert b._access_code == access_code
    assert b._retrieve_interval == retrieve_interval
    assert isinstance(b._retriever, ItemRetriever)
