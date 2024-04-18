from .author import Author
from .category import Category
from .content_field import ContentField
from .feed import Feed
from .page import Page
from .post import Post
from .tag import Tag


class ButterCMS(object):
    """ButterCMS"""
    def __init__(self, auth_token):
        self.authors = Author(auth_token)
        self.categories = Category(auth_token)
        self.tags = Tag(auth_token)
        self.content_fields = ContentField(auth_token)
        self.feeds = Feed(auth_token)
        self.pages = Page(auth_token)
        self.posts = Post(auth_token)
