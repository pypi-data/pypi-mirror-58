def elements(url: str, selector: str, cache=True):
    import requests_cache
    import lxml.html
    import requests
    from lxml.cssselect import CSSSelector

    """
        Access the link and return elements filtered by CSS selector.
    :param url: link to be accessed;
    :param selector: selector to be applied;
    :param cache: You can use a cache layer;
    :return: list of elements;
    """
    if cache:
        requests_cache.install_cache('cache')

    response = requests.get(url)
    content = lxml.html.fromstring(response.content)
    els = CSSSelector(selector)(content)

    def parse(element):
        dic = {'text': element.text}
        dic.update(element.attrib)
        return dic
    els = list(map(parse, els))

    return els


def download(url: str, path: str):
    """
        Download the file of link to path.
    :param url: link to be downloaded;
    :param path: path folder to download the file;
    :return: return the full file path;
    """
    import os
    import urllib
    from requests.utils import requote_uri
    name = url.split('/')[-1]
    filepath = os.path.join(path, name)
    url = requote_uri(url)
    if not os.path.isfile(filepath):
        try:
            urllib.request.urlretrieve(url, filepath)
        except urllib.error.HTTPError as e:
            print("%s %s" % (e, url))
            filepath = None
    return filepath
