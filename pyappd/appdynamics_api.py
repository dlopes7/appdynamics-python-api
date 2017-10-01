import requests
from typing import List

from .operations import Operation
from .mapper import map_from_json

from .models import Application, Tier

from .logger import log

class AppDynamicsApi:

    def __init__(self, controller_url, user, password, tenant='customer1'):
        self.controller_url = controller_url
        self.user = user
        self.password = password
        self.auth = ('{}@{}'.format(user, tenant), password)
        self.tenant = tenant
        self.params = {'output': 'json'}

    def _make_request(self, operation):
        
        log.debug('Executing operation {}'.format(operation))
        url = '{}/{}'.format(self.controller_url, operation.uri)
        response = requests.request(operation.method,
                                    url,
                                    params=self.params, 
                                    auth=self.auth)
        log.debug('Response: {}'.format(response))
        return map_from_json(operation, response.json())

    def get_applications(self):
        operation = Operation('GET', 'controller/rest/applications', Application, api=self)
        return self._make_request(operation)

    def get_application(self, app):       
        operation = Operation('GET', 'controller/rest/applications/{}'.format(app), Application, api=self)
        return self._make_request(operation)

    def get_tiers(self, app):

        if hasattr(app, 'app_id'):
            app = app.app_id

        operation =  Operation('GET', 'controller/rest/applications/{}/tiers'.format(app), Tier, api=self)
        return self._make_request(operation)
    