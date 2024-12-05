import requests
import os
import dotenv
from app.utils import handle_request_errors

dotenv.load_dotenv()

refresh_token = os.getenv("REFRESH_TOKEN")
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
redirect_uri = os.getenv("REDIRECT_URI")
token_url = os.getenv("TOKEN_URL")
scope = os.getenv("SCOPE")

def get_access_token():
    """
    Utility function to get the access token.

    This function sends a POST request to the token URL with the necessary
    parameters to obtain a new access token using a refresh token. If the
    request is successful, it returns the token information as a JSON object.
    In case of an error, it handles the exception using the handle_request_errors
    function.

    Returns:
        dict: A dictionary containing the access token information.

    Raises:
        requests.exceptions.RequestException: If there is an issue with the request.
    """
    try:
        resp = requests.post(token_url, {
            "refresh_token": refresh_token,
            "grant_type": "refresh_token",
            "client_id": client_id,
            "client_secret": client_secret,
            "redirect_uri": redirect_uri,
            "scope": scope
        }, timeout=5)
        resp.raise_for_status()
        token = resp.json()
    except Exception as e:
        handle_request_errors(e, token_url)

    return token