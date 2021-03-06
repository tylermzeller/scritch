import scritch.config.scritch_config as config
import scritch.requester.request as requester
from scritch.util import abs_path, get_filenames, url_to_filename


def run(work, *args, url=config.URL, cache=config.CACHE):
    if not url:
        print('Config Error: URL not provided')
        exit()

    if cache:
        filename = url_to_filename(url.lower())
        path = f'{abs_path(__file__)}/../raw_data'
        if filename in get_filenames(path, set=True):
            print(f'Reading from cache: {filename}')
            with open(f'{path}/{url_to_filename(url)}', 'r') as f:
                raw_html = f.read()
        else:
            raw_html = requester.simple_get_html(url)
            print(f'Saving to cache: {filename}')
            with open(f'{path}/{url_to_filename(url)}', 'w') as f:
                f.write(raw_html.decode())
    else:
        raw_html = requester.simple_get_html(url)
    return work(raw_html, url, *args)
