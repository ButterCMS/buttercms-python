import unittest
from author import Author
from butter_cms import ButterCMS
from category import Category
from content_field import ContentField
from feed import Feed
from post import Post
auth_token = ''
# TODO: Add auth_token before running test


class TestButterCMS(unittest.TestCase):
    def test_members(self):
        client = ButterCMS(auth_token)
        self.assertIsInstance(client.authors, Author)
        self.assertIsInstance(client.categories, Category)
        self.assertIsInstance(client.content_fields, ContentField)
        self.assertIsInstance(client.feeds, Feed)
        self.assertIsInstance(client.posts, Post)


class TestAPI(unittest.TestCase):
    def is_ok_request(self, response):
        try:
            # Check for successful api state
            self.assertIn('data', response)
        except AssertionError:
            # Check for error api state
            self.assertIn('detail', response)


class TestAuthor(TestAPI):
    def test_all(self):
        author = Author(auth_token)
        response = author.all()
        self.is_ok_request(response)

    def test_all_include(self):
        author = Author(auth_token)
        response = author.all(include='recent_posts')
        self.is_ok_request(response)
        for post in response['data']:
            self.assertIn('recent_posts', post)

    def test_get(self):
        author = Author(auth_token)
        response = author.get('adam-yala')
        self.is_ok_request(response)


class TestCategory(TestAPI):
    def test_all(self):
        category = Category(auth_token)
        response = category.all()
        self.is_ok_request(response)

    def test_all_include(self):
        category = Category(auth_token)
        response = category.all(include='recent_posts')
        self.is_ok_request(response)
        for category_post in response['data']:
            self.assertIn('recent_posts', category_post)

    def test_get(self):
        category = Category(auth_token)
        response = category.get('beer')
        self.is_ok_request(response)


class TestContentField(TestAPI):
    def test_get(self):
        content_field = ContentField(auth_token)
        response = content_field.get(['homepage_headline', 'homepage_title'])
        self.is_ok_request(response)


class TestFeed(TestAPI):
    def test_get_rss(self):
        feed = Feed(auth_token)
        response = feed.get('rss')
        self.is_ok_request(response)

    def test_get_atom(self):
        feed = Feed(auth_token)
        response = feed.get('atom')
        self.is_ok_request(response)

    def test_get_sitemap(self):
        feed = Feed(auth_token)
        response = feed.get('sitemap')
        self.is_ok_request(response)


class TestPost(TestAPI):
    def test_all(self):
        post = Post(auth_token)
        response = post.all()
        self.is_ok_request(response)
        response = post.all(page=1, page_size=10)
        self.is_ok_request(response)

    def test_search(self):
        post = Post(auth_token)
        response = post.search('test')
        self.is_ok_request(response)
        response = post.search('test', page=1, page_size=10)
        self.is_ok_request(response)

    def test_get(self):
        post = Post(auth_token)
        response = post.get('test-post')
        self.is_ok_request(response)

if __name__ == '__main__':
    unittest.main()
