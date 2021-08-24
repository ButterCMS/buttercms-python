from .client import Client


class Post(Client):
    """Post"""
    def __init__(self, auth_token):
        Client.__init__(self, auth_token)
        self.path = 'posts/'

    def all(self, params=None):
        return self.api_get(params=params)

    def get(self, slug):
        full_slug = '{}/'.format(slug)
        return self.api_get(slug=full_slug)

    def search(self, query, params=None):
        slug = 'search/'
        if not params:
            params = {
                'query': query,
            }
        else:
            params['query'] = query
        return self.api_get(slug=slug, params=params)
