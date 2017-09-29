class Application:
    def __init__(self, json_object):
        self.app_id = json_object['id']
        self.name = json_object['name']
        self.description = json_object['description']
        
        self.raw = json_object

    def build_from_json(json_object):
        return Application(json_object)

    def __str__(self):
        return 'Application ID: {}\t NAME: {}'.format(self.app_id, self.name)

