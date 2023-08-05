import requests
from riot.connection import (
    get_headers, get_base_url, get_main_params)


class APIRequestException(Exception):
    pass


class APIRequest():
    url = ''
    data = {}

    def __init__(self, url):
        self.url = url
        self.data = {}

        if self.url == '':
            raise APIRequestException('url is required')

    def get(self, region):
        url_str = 'https://{base}{url}'.format(
            base=get_base_url(region),
            url=self.url
        )
        headers = get_headers()
        params = get_main_params()

        try:
            response = requests.get(url_str, params=params , headers=headers)
            self.data = response.json()
            return (response.status_code == 200)
        except Exception as ex:
            self.data = {'status': {'message': str(ex), 'status_code': 500}}
            return False

        self.data = {}
        return False
