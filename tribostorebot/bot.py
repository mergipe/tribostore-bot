from tribostorebot.scraper import Scraper

class TriboStoreBot:

    def __init__(self, token, request_url, fetch_interval):
        self.token = token
        self.fetch_interval = fetch_interval
        self.scraper = Scraper(request_url)
