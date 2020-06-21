import logging
import re
import telegram
import telegram.ext

from tribostorebot.items import ItemRetriever


class TriboStoreBot:

    def __init__(self, token, access_code, request_url, retrieve_interval):
        self._token = token
        self._access_code = access_code
        self._retrieve_interval = retrieve_interval
        self._retriever = ItemRetriever(request_url)
