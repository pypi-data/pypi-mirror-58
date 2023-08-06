from requests import get
from requests.exceptions import RequestException
from contextlib import closing


def simple_get(url: str) -> bytes:
    """
    Attempts to get the content at `url` by making an HTTP GET request.
    If the content-type of response is some kind of HTML/XML, return the
    text content, otherwise return None.
    """
    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None

    except RequestException as e:
        log_error(f'Error during requests to {url} : {str(e)}')
        return None


def raw_get(url: str):
    try:
        with closing(get(url, allow_redirects=True)) as resp:
            return resp

    except RequestException as e:
        log_error(f'Error during requests to {url} : {str(e)}')
        return None


def is_good_response(resp) -> bool:
    """
    Returns True if the response seems to be HTML, False otherwise.
    """
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200
            and content_type is not None
            and (content_type.find('html') > -1 or content_type.find('json') > -1))


def log_error(e: str):
    """
    It is always a good idea to log errors. 
    This function just prints them, but you can
    make it do anything.
    """
    print(e)
