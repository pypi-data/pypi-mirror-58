# Project description
confluence-cloud-ashwani
confluence-cloud-ashwani is an API wrapper for Atlassian Confluence written in Python

### Installing
`pip install confluence-cloud-python`

### Usage
Client instantiation

`from sigconfluence.client import Client`

`client = Client('CLIENT_ID', 'CLIENT_SECRET')`

# OAuth 2.0 (3LO)

For more information: https://developer.atlassian.com/cloud/jira/platform/oauth-2-authorization-code-grants-3lo-for-apps/

Direct the user to the authorization URL to get an authorization code

A refresh token can be returned with the access token in your initial authorization flow. To do this, add the offline_access scope to the scope parameter of the authorization URL.

`scope_list = ['read:confluence-space.summary', 'offline_access','read:confluence-props','read:confluence-content.all', 'read:confluence-content.summary', 'search:confluence']`

`url = client.authorization_url('REDIRECT_URI', scope_list, 'STATE')`

### Exchange authorization code for access token

`response = client.exchange_code('REDIRECT_URI', 'CODE')`

### Set access token in the library

`client.set_access_token('ACCESS_TOKEN')`

### Get the cloudid for your site

`response = client.get_resource_list()`

### Set cloudid in the library

`client.set_cloud_id('CLOUD_ID')`

### Refresh token

`response = client.refresh_token('REFRESH_TOKEN')`

### Find all the Confluence Spaces

`spaces = client.spaces.get_spaces()`

### Find all the contents 

```python
start = 0
limit = 100
contents_data = client.contents.get_contents('expand=body.storage&next=true&limit='+str(limit)+'&start='+str(start))
contents.extend(contents_data['results'])
start=limit
limit=contents_data['size']

print contents
```

