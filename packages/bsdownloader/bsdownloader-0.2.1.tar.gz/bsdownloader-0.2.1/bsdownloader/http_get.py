from requests import get
from requests.exceptions import RequestException
from contextlib import closing
import os


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
        return None


def download_file(url: str, file: str, p_fun) -> bool:
    try:
        with open(file, mode="wb") as f:
            resp = get(url, stream=True, allow_redirects=True)
            total_length = resp.headers.get("content-length")
            if total_length is None:
                f.write(resp.content)
            else:
                dl = 0
                total_length = int(total_length)
                for data in resp.iter_content(chunk_size=1024):
                    dl += len(data)
                    p_fun(int(dl / total_length * 100.0))
                    f.write(data)
        return True
    except RequestException:
        if os.path.isfile(file):
            os.remove(file)
        return False


def is_good_response(resp) -> bool:
    """
    Returns True if the response seems to be HTML, False otherwise.
    """
    content_type = resp.headers["Content-Type"].lower()
    return (
        resp.status_code == 200
        and content_type is not None
        and (content_type.find("html") > -1 or content_type.find("json") > -1)
    )
