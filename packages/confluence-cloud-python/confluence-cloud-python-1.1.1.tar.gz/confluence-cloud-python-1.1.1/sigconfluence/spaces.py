class Spaces(object):
    def __init__(self, client):
        self._client = client

    def get_spaces(self, params=None):
        """
        Returns projects visible to the user.

        This operation can be accessed anonymously.
        """
        return self._client._get(self._client._BASE_URL + 'space', params=params)