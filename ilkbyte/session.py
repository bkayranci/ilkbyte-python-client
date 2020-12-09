from typing import Union, Text
import requests
from requests import Response


class IlkbyteAPISession(requests.Session):

    def __init__(self, host: str, secret_key: str, access_key: str):
        super().__init__()

        self.headers.update({
            'Accept-Charset': 'utf-8',
            'Content-Type': 'application/json',
            'User-Agent': 'ilkbyte-python-client'
        })
        self._host = host
        self._secret_key = secret_key
        self._access_key = access_key

    def __get_auth_params(self):
        return {
            'secret': self._secret_key,
            'access': self._access_key
        }

    def get_resource(self, resource: str, **kwargs):
        url = f"{self._host}/{resource}"

        if 'params' in kwargs:

            kwargs['params'].update(self.__get_auth_params())
        else:
            kwargs['params'] = self.__get_auth_params()

        return self.get(url, **kwargs)

    def get(self, url: Union[Text, bytes], **kwargs) -> Response:
        response = super(IlkbyteAPISession, self).get(url, **kwargs)
        return response
