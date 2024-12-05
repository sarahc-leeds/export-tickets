from auth import get_access_token

token = get_access_token()

print(token['access_token'])