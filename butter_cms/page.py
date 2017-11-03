from .client import Client


class Page(Client):
    """Page"""
    def __init__(self, auth_token):
        Client.__init__(self, auth_token)
        self.path = 'pages/'

    def list(self, slug, params=None):
        full_slug = '{}/'.format(slug)
        return self.api_get(slug=full_slug, params=params)

    def get(self, slug1, slug2, params=None):
        full_slug = '{}/{}/'.format(slug1, slug2)
        return self.api_get(slug=full_slug, params=params)
