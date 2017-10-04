"""
AppDynamucsApi
~~~~~~~~~~~~~~

Core of the api.
"""
import requests

from .models import Application, Tier, Dashboard, Operation

from .utils.logger import log
from .utils.mapper import map_from_json


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

    def _make_request(self, operation, internal=False):
        """
        Private method that takes in an Operation object and invokes the HTTP request

        :param operation: `Operation` that will be invoked.
        """
        with requests.Session() as session:
            log.debug('Executing operation %s', operation)
            headers = {}

            if internal:
                cookie = self._login(session)
                headers = {'X-CSRF-TOKEN': cookie,
                           'accept': 'application/json'}

            url = '{}/{}'.format(self.controller_url, operation.uri)
            response = session.request(operation.method,
                                       url,
                                       params=self.params,
                                       auth=self.auth,
                                       headers=headers)
            log.debug('Response: %s', response)

            if response.status_code >= 400:
                log.error('Error calling the api %s, URL: %s',
                          response.status_code, url)
                return []

            return map_from_json(operation, response.json())

    def _login(self, session):
        url = '{}/{}'.format(self.controller_url, 'auth')
        res = session.get(url, params={'action': 'login'}, auth=self.auth)
        cookie = res.cookies['X-CSRF-TOKEN']
        log.debug('Internal API, Login: %s, Cookie: %s',
                  res, cookie)

        return cookie

    def get_applications(self):
        """
        Gets all Business Applications from a controller

        """
        operation = Operation(
            'GET', 'controller/rest/applications', Application, api=self)
        return self._make_request(operation)

    def get_application(self, app):
        """
        Gets one Business Application from the controller

        :param application: Application Name or Application ID.
        """
        operation = Operation(
            'GET', 'controller/rest/applications/{}'.format(app), Application, api=self)
        return self._make_request(operation)

    def get_tiers(self, app):
        """
        Gets all tiers from one application

        :param application: `Application` object, Application Name or Application ID.
        """

        if hasattr(app, 'app_id'):
            app = app.app_id

        operation = Operation(
            'GET', 'controller/rest/applications/{}/tiers'.format(app), Tier, api=self)
        return self._make_request(operation)

    def get_dashboards(self):
        operation = Operation(
            'GET', 'controller/restui/dashboards/getAllDashboardsByType/false', Dashboard)
        return self._make_request(operation, internal=True)
