import unittest
from .author import Author
from .category import Category
from .tag import Tag
from .content_field import ContentField
from .feed import Feed
from .page import Page
from .post import Post
auth_token = 'f97d131d955f48af0769a4c827bb47728cbd5d05'


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
        response = author.all(params={'include':'recent_posts'})
        self.is_ok_request(response)
        for post in response['data']:
            self.assertIn('recent_posts', post)

    def test_get(self):
        author = Author(auth_token)
        response = author.get('adam-yala')
        self.is_ok_request(response)

    def test_get_include(self):
        author = Author(auth_token)
        response = author.get(params={'include':'recent_posts'})
        self.is_ok_request(response)
        for post in response['data']:
            self.assertIn('recent_posts', post)


class TestCategory(TestAPI):
    def test_all(self):
        category = Category(auth_token)
        response = category.all()
        self.is_ok_request(response)

    def test_all_include(self):
        category = Category(auth_token)
        response = category.all(params={'include':'recent_posts'})
        self.is_ok_request(response)
        for category_post in response['data']:
            self.assertIn('recent_posts', category_post)

    def test_get(self):
        category = Category(auth_token)
        response = category.get('beer')
        self.is_ok_request(response)

    def test_get_include(self):
        category = Category(auth_token)
        response = category.get(params={'include':'recent_posts'})
        self.is_ok_request(response)
        for post in response['data']:
            self.assertIn('recent_posts', post)


class TestTag(TestAPI):
    def test_all(self):
        tag = Tag(auth_token)
        response = tag.all()
        self.is_ok_request(response)

    def test_all_include(self):
        tag = Tag(auth_token)
        response = tag.all(params={'include':'recent_posts'})
        self.is_ok_request(response)
        for tag_post in response['data']:
            self.assertIn('recent_posts', tag_post)

    def test_get(self):
        tag = Tag(auth_token)
        response = tag.get('beer')
        self.is_ok_request(response)

    def test_get_include(self):
        tag = Tag(auth_token)
        response = tag.get(params={'include':'recent_posts'})
        self.is_ok_request(response)
        for post in response['data']:
            self.assertIn('recent_posts', post)


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


class TestPage(TestAPI):
    def test_get(self):
        page = Page(auth_token)
        response = page.get('news', 'hello-world')
        self.is_ok_request(response)


class TestPost(TestAPI):
    def test_all(self):
        post = Post(auth_token)
        response = post.all()
        self.is_ok_request(response)
        response = post.all({'page': 1, 'page_size': 10})
        self.is_ok_request(response)

    def test_search(self):
        post = Post(auth_token)
        response = post.search('test')
        self.is_ok_request(response)
        response = post.search('test', {'page': 1, 'page_size': 10})
        self.is_ok_request(response)

    def test_get(self):
        post = Post(auth_token)
        response = post.get('test-post')
        self.is_ok_request(response)


if __name__ == '__main__':
    unittest.main()
