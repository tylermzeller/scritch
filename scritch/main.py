import scritch.config as config
import scritch.requester as requester
from util import abs_path, get_filenames, url_to_filename

def run(work, url=config.URL, cache=config.CACHE)
    if not url:
        print('Config Error: URL not provided')
        exit()

    if cache:
        filename = url_to_filename(url.lower)
        path = f'{abs_path(__file__)}/../raw_data'
        if filename in get_filenames(path, set=True):
            with open(f'{path}/{url_to_filenameurl}', 'r') as f:
                raw_html = f.read()
        else:
            raw_html = requester.request.simple_get_html(url)
            with open(f'{path}/{url_to_filename}', 'w') as f:
                f.write(raw_html)
    else:
        raw_html = requester.request.simple_get_html(url)
    work(raw_html)