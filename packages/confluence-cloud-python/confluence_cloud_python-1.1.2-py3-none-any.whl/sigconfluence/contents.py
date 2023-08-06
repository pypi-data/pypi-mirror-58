class Contents(object):
    def __init__(self, client):
        self._client = client

    def get_contents(self, params=None):
        """
        Returns projects visible to the user.

        This operation can be accessed anonymously.
        """
        return self._client._get(self._client._BASE_URL + 'content', params=params)
    
    def search_for_contents_using_cql(self, data):
        """
        Searches for contents using CQL.

        There is a GET version of this resource that can be used for smaller CQL query expressions.

        This operation can be accessed anonymously.
        """
        return self._client._post(self._client._BASE_URL + 'content/search', json=data)