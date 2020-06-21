from tribostorebot.items import ItemRetriever


class TriboStoreBot:

    def __init__(self, token, request_url, retrieve_interval):
        self.token = token
        self.retrieve_interval = retrieve_interval
        self.retriever = ItemRetriever(request_url)
