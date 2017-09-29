from .models import Application

class Operation:
    def __init__(self, method, uri, model):
        self.method = method
        self.uri = uri
        self.model = model

GET_ALL_APPLICATIONS = Operation('GET', 'controller/rest/applications', Application)
