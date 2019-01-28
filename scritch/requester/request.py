from requests import get
from requests.exceptions import RequestException
from contextlib import closing

def simple_get_html(url):
    try:
        with closing(get(url, stream=True)) as resp:
            if _is_good_response(resp):
                return resp.content
            else:
                return None

    except RequestException as e:
        _log_error(f'Error during requests to {url} : {str(e)}')
        return None


def _is_good_response(resp):
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200
            and content_type is not None
            and content_type.find('html') > -1)


def _log_error(e):
    print(e)
