from .client import Client


class Category(Client):
    """Category"""
    def __init__(self, auth_token):
        Client.__init__(self, auth_token)
        self.path = 'categories/'

    def all(self, params=None):
        return self.api_get(params=params)
