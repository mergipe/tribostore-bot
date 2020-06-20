from tribostorebot.scraper import Scraper

def test_scraper_instantiation():
    url = 'test_url'
    s = Scraper(url)
    assert s.url == url
