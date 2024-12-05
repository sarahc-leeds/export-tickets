def handle_request_errors(e, url):
    """
    Handles errors that occur during an HTTP request.
    Args:
        e (Exception): The exception that was raised during the request.
        url (str): The URL that was being requested when the error occurred.
    Prints the error message and the URL, then exits the program with a status code of 1.
    """
    print(f"Error while requesting {url}")
    print(e)
    exit(1)