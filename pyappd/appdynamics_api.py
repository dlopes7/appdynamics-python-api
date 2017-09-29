import requests
from typing import List

from .operations import *
from .mapper import map_from_json

from .models import Application

class AppDynamicsApi:

    def __init__(self, controller_url, user, password, tenant='customer1'):
        self.controller_url = controller_url
        self.user = user
        self.password = password
        self.auth = ('{}@{}'.format(user, tenant), password)
        self.tenant = tenant

    def _make_request(self, operation):
        url = '{}/{}'.format(self.controller_url, operation.uri)
        response = requests.request(operation.method, url, params={'output': 'json'}, auth=self.auth)
        return map_from_json(operation, response.json())

    def get_applications(self):
        return self._make_request(GET_ALL_APPLICATIONS)

    