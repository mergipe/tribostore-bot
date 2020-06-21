from tribostorebot.items import ItemRetriever


class TriboStoreBot:

    def __init__(self, token, request_url, fetch_interval):
        self.token = token
        self.fetch_interval = fetch_interval
        self.retriever = ItemRetriever(request_url)
