"""
A class for making requests to the social network Instagram used mobile API
"""
import requests
import json

import config


class RequestsWorker:

    def __init__(self, host_proxy: str = '', port_proxy: int = 0):
        self.portal_url = config.PORTAL_URL
        self.request = requests
        self.host_proxy = host_proxy
        self.port_proxy = port_proxy
        self.proxies = dict()
        if self.host_proxy and self.port_proxy:
            self.proxies.update({'https': self.host_proxy + ":" + str(self.port_proxy)})

    def make_request_post(self, url: str, params: dict, headers: dict, cookie: dict = None) -> dict:
        """
        :param headers:
        :param url: str
        :param params: dict
        :param cookie: dict
        :return: dict
        """
        try:
            if not self.proxies:
                response = self.request.post(url, data=params, headers=headers, cookies=cookie)
                print(response.url, response.status_code)
                print('*' * 100)
            else:
                response = self.request.post(url, data=params, headers=headers, cookies=cookie,
                                             proxies=self.proxies)
            try:
                data = response.json()
            except json.JSONDecodeError as error:
                return {"status": False, "error": True, "error_type": 'json_error', "text": error}
        except requests.exceptions.ConnectionError as error:
            return {"status": False, "error": True, "error_type": 'connect_error', "text": error}

        try:
            response.raise_for_status()
        except requests.HTTPError as error:
            if response.status_code == 400 and data["message"] == "challenge_required":
                return {"status": False, "error": True, "error_type": data["error_type"], "text": error,
                        "http_error": response.status_code}
            return {"status": False, "error": True, "error_type": 'http_error', "text": error,
                    "http_error": response.status_code}

        if response.status_code == 200:
            data = json.loads(response.text)
            if data["status"] == 'ok':
                return {"status": True, "data": data, 'cookies': response.cookies, "headers": response.headers}

        return {"status": False, "error": True, "error_type": 'fail', "text": data}

    def make_request_get(self, url: str, params: dict, headers: dict, cookies: dict = None,
                         is_params: bool = True, is_hmac: bool = True) -> dict:
        """
        :param headers:
        :param url: str
        :param params: dict
        :param cookies:dict
        :param is_params bool
        :param is_hmac bool (if need SIGNATURE - True)
        :return: dict
        """
        try:
            if not self.proxies:
                if is_params:
                    response = self.request.get(url, params=params, headers=headers, cookies=cookies)
                else:
                    response = self.request.get(url, headers=headers, cookies=cookies)
                print(response.url, response.status_code)
                print('*' * 100)
            else:
                if is_params:
                    response = self.request.get(url, params=params, headers=headers, cookies=cookies,
                                                proxies=self.proxies)
                else:
                    response = self.request.get(url, headers=headers, cookies=cookies,
                                                proxies=self.proxies)
            try:
                data = response.json()
            except json.JSONDecodeError as error:
                return {"status": False, "error": True, "error_type": 'json_error', "text": error}
        except requests.exceptions.ConnectionError as error:
            return {"status": False, "error": True, "error_type": 'connect_error', "text": error}

        try:
            response.raise_for_status()
        except requests.HTTPError as error:
            return {"status": False, "error": True, "error_type": 'http_error', "text": error,
                    "http_error": response.status_code}

        if response.status_code == 200:
            try:
                if data["status"] == 'ok':
                    return {"status": True, "data": data, "headers": response.headers, 'cookies': response.cookies}
            except KeyError as error:
                return {"status": False, "error": True, "error_type": 'key_error', "text": error}

        return {"status": False, "error": True, "error_type": 'fail', "text": data}