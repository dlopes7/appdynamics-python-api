class Application:
    def __init__(self, json_object, api):
        self.app_id = json_object['id']
        self.name = json_object['name']
        self.description = json_object['description']
        
        self.raw = json_object

        self.api = api

    @staticmethod
    def build_from_json(json_object, operation):
        return Application(json_object, operation.api)

    def get_tiers(self):
        """
        Gets all tiers from this application

        """
        return self.api.get_tiers(self)

    def __str__(self):
        return 'Application ID: {}\t NAME: {}'.format(self.app_id, self.name)

