"""
Operation
~~~~~~~~~

This class holds all that is necessary for the HTTP operation
"""



class Operation:
    """
    Simple class with data necessary to make the HTTP request and construct a model object

    """

    def __init__(self, method, uri, model, api=None):
        self.method = method
        self.uri = uri
        self.model = model

    def __str__(self):
        return '{}: {}\t'.format(self.method, self.uri)
