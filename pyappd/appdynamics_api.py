"""
AppDynamucsApi
~~~~~~~~~~~~~~

Core of the api.
"""
import requests

from .operations import Operation
from .mapper import map_from_json

from .models import Application, Tier

from .logger import log

class AppDynamicsApi:
    """
    This is the core class
    It has methods that directly interact with the Api
    """

    def __init__(self, controller_url, user, password, tenant='customer1'):
        self.controller_url = controller_url
        self.user = user
        self.password = password
        self.auth = ('{}@{}'.format(user, tenant), password)
        self.tenant = tenant
        self.params = {'output': 'json'}

    def _make_request(self, operation):
        """
        Private method that takes in an Operation object and invokes the HTTP request

        :param operation: `Operation` that will be invoked.
        """

        log.debug('Executing operation %s', operation)
        url = '{}/{}'.format(self.controller_url, operation.uri)
        response = requests.request(operation.method,
                                    url,
                                    params=self.params,
                                    auth=self.auth)
        log.debug('Response: %s', response)
        return map_from_json(operation, response.json())

    def get_applications(self):
        """
        Gets all Business Applications from a controller

        """
        operation = Operation('GET', 'controller/rest/applications', Application, api=self)
        return self._make_request(operation)

    def get_application(self, app):
        """
        Gets one Business Application from the controller

        :param application: Application Name or Application ID.
        """
        operation = Operation('GET', 'controller/rest/applications/{}'.format(app), Application, api=self)
        return self._make_request(operation)

    def get_tiers(self, app):
        """
        Gets all tiers from one application

        :param application: `Application` object, Application Name or Application ID.
        """

        if hasattr(app, 'app_id'):
            app = app.app_id

        operation =  Operation('GET', 'controller/rest/applications/{}/tiers'.format(app), Tier, api=self)
        return self._make_request(operation)
    