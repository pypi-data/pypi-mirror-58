import os
import json
import requests


class RezeClient:
    def __init__(self, app_id, app_key, server_url=None):
        """
        :param app_id: your app id
        :param app_key: your app key
        """

        self.app_id = app_id
        self.app_key = app_key
        self.base_url = os.environ.get('SERVER_URL')
        if self.base_url is None:
            self.base_url = server_url
        if self.base_url is None:
            self.base_url = 'http://localhost:5000'

    def send(self, request):
        url = self.base_url + request.path
        try:
            if request.method == 'PUT':
                return self.__put(request, url)
            if request.method == "GET":
                return self.__get(request, url)
            if request.method == 'POST':
                return self.__post(request, url)
            if request.method == "DELETE":
                return self.__delete(request, url)
        except Exception as e:
            print(str(e))

    def __put(self, request, url):
        response = requests.put(url, headers=self.__get_headers(), data=json.dumps(request.get_body_parameters()))
        return response.json()

    def __get(self, request, url):
        response = requests.get(url, headers=self.__get_headers(), data=json.dumps(request.get_body_parameters()))
        return response.json()

    def __post(self, request, url):
        response = requests.post(url, headers=self.__get_headers(), data=request.get_body_parameters())
        return response.json()

    def __delete(self, request, url):
        response = requests.delete(url, headers=self.__get_headers(), data=request.get_body_parameters())
        return response.json()

    def __get_headers(self):
        header = dict()
        header['appId'] = self.app_id
        header['appKey'] = self.app_key
        return header
