from butter_cms.feed import Feed
from requests.exceptions import HTTPError
from test_vcr_config import TestCaseWithAPIKey, vcr_setup

vcr = vcr_setup()

class TestFeed(TestCaseWithAPIKey):
    @vcr.use_cassette('feeds/test_feed_sitemap_invalid_token.json')
    def test_invalid_token(self):
        with self.assertRaises(HTTPError):
            feed = Feed('invalid_token')
            feed.get('sitemap')

    @vcr.use_cassette('feeds/test_feed_sitemap.json')
    def test_get_sitemap_feed(self):
        feed = Feed(self.token)
        response = feed.get('sitemap')

        self.assertIsNotNone(response)
        self.assertIn('data', response)

        data = response['data']
        self.assertIn('<?xml version="1.0" encoding="UTF-8"?>', data)
        self.assertIn('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.sitemaps.org/schemas/sitemap/0.9 http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd">', data)

    @vcr.use_cassette('feeds/test_feed_rss.json')
    def test_get_rss_feed(self):
        feed = Feed(self.token)
        response = feed.get('rss')

        self.assertIsNotNone(response)
        self.assertIn('data', response)

        data = response['data']
        self.assertIn('<?xml version="1.0" encoding="UTF-8"?>', data)
        self.assertIn('<rss xmlns:atom="http://www.w3.org/2005/Atom" xmlns:content="http://purl.org/rss/1.0/modules/content/" xmlns:media="http://search.yahoo.com/mrss/" version="2.0">', data)

    @vcr.use_cassette('feeds/test_feed_atom.json')
    def test_get_atom_feed(self):
        feed = Feed(self.token)
        response = feed.get('atom')

        self.assertIsNotNone(response)
        self.assertIn('data', response)

        data = response['data']
        self.assertIn('<?xml version="1.0" encoding="UTF-8"?>', data)
        self.assertIn('<feed xmlns="http://www.w3.org/2005/Atom" xml:lang="en-us">', data)

    @vcr.use_cassette('feeds/test_feed_non_existent.json')
    def test_get_non_existent_feed(self):
        with self.assertRaises(HTTPError):
            feed = Feed(self.token)
            response = feed.get('non-existent')

            self.assertIsNotNone(response)
            self.assertIn('detail', response)
            self.assertEqual('Not found', response['detail'])