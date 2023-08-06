import logging

try:
    from urllib import quote_plus
    from urlparse import urljoin, urlparse, parse_qs
except ImportError:
    from urllib.parse import quote_plus, urljoin, urlparse, parse_qs

import requests

from app_scraper import settings as s

log = logging.getLogger(__name__)


def default_headers():
    return {
        "Origin": "https://www.google.com",
        "User-Agent": s.USER_AGENT,
        "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
    }

def build_url(method, id_string, website):
    """Creates the absolute url for a type of object. E.g. details, developer,
    or similar.
    :param method: the corresponding method to get for an id.
    :param id_string: an id string query parameter.
    :return: a URL string.
    """

    url = "{base}/?id={id}".format(base=website, id=id_string)
    return url


def send_request(
    method,
    url,
    data=None,
    params=None,
    headers=None,
    timeout=30,
    verify=True,
    allow_redirects=False,
):
    """Sends a request to the url and returns the response.
    :param method: HTTP method to use.
    :param url: URL to send.
    :param data: Dictionary of post data to send.
    :param headers: Dictionary of headers to include.
    :param timeout: number of seconds before timing out the request
    :param verify: a bool for requesting SSL verification.
    :return: a Response object.
    """
    data = {} if data is None else data
    params = {} if params is None else params
    headers = default_headers() if headers is None else headers

    try:
        response = requests.request(
            method=method,
            url=url,
            data=data,
            params=params,
            headers=headers,
            timeout=timeout,
            verify=verify,
            allow_redirects=allow_redirects,
        )
        if not response.status_code == requests.codes.ok:
            response.raise_for_status()
    except requests.exceptions.RequestException as e:
        log.error(e)
        raise

    return response


def parse_app_details(soup):
    """Extracts an app's details from its info page.
    :param soup: a strained BeautifulSoup object of an app
    :return: a dictionary of app details
    """
    title = soup.select_one('h1[itemprop="name"] span').text
    icon = soup.select_one('img[class="T75of sHb2Xb"]').attrs["src"].split("=")[0]
    editors_choice = bool(soup.select_one('meta[itemprop="editorsChoiceBadgeUrl"]'))

    # Main category will be first
    category = [
        c.attrs["href"].split("/")[-1] for c in soup.select('a[itemprop="genre"]')
    ]

    description_soup = soup.select_one('div[itemprop="description"] span div')
    if description_soup:
        description = "\n".join(description_soup.stripped_strings)
        description_html = description_soup.encode_contents()
    else:
        description = description_html = None

    try:
        changes_soup = soup.select('div[itemprop="description"] content')[1]
        recent_changes = "\n".join(
            [x.string.strip() if x.string is not None else "" for x in changes_soup]
        )
    except (IndexError, AttributeError):
        recent_changes = None

    try:
        dev_id = soup.select_one("a.hrTbp.R8zArc").attrs["href"].split("=")[1]
    except IndexError:
        dev_id = None
    developer_id = dev_id if dev_id else None

    data = {
        "title": title,
        "icon": icon,
        "category": category,
        "description": description,
        "description_html": description_html,
        "recent_changes": recent_changes,
        "editors_choice": editors_choice,
        "developer_id": developer_id,
    }
    return data

