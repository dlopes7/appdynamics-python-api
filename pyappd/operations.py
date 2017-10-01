from .models import Application, Tier

class Operation:
    def __init__(self, method, uri, model, api=None):
        self.method = method
        self.uri = uri
        self.model = model
        self.api = api

    
    def __str__(self):
        return '{}: {}\t'.format(self.method, self.uri)
