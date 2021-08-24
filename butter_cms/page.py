from .client import Client


class Page(Client):
    """Page"""
    def __init__(self, auth_token):
        Client.__init__(self, auth_token)
        self.path = 'pages/'

    def all(self, page_type, params=None):
        full_slug = '{}/'.format(page_type)
        return self.api_get(slug=full_slug, params=params)

    def get(self, page_type, page_slug, params=None):
        full_slug = '{}/{}/'.format(page_type, page_slug)
        return self.api_get(slug=full_slug, params=params)

    def search(self, query, params=None):
        slug = 'search/'
        if not params:
            params = {
                'query': query,
            }
        else:
            params['query'] = query
        return self.api_get(slug=slug, params=params)
