from bs4 import BeautifulSoup


def get_all_selector(html, selector):
    if isinstance(html, str) or isinstance(html, bytes):
        return BeautifulSoup(html, 'html.parser').select(selector=selector)
    return html.select(selector=selector)


def get_all_links(html):
    return get_all_selector(html, 'a')


def get_links(html, quantifier=all, **kwargs):
    return list(filter(lambda a: quantifier([val(a.get(key)) for key, val in kwargs.items()]),
                       get_all_links(html)))
