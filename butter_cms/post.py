from client import Client


class Post(Client):
    """Post"""
    def __init__(self, auth_token):
        Client.__init__(self, auth_token)
        self.path = 'posts/'

    def all(self, page=1, page_size=10):
        params = {
            'page': page,
            'page_size': page_size,
        }
        return self.api_get(params=params)

    def search(self, query='', page=1, page_size=10):
        params = {
            'query': query,
            'page': page,
            'page_size': page_size,
        }
        return self.api_get(params=params)
