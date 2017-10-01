class Tier:
    def __init__(self, json_object, api):
        self.tier_id = json_object['id']
        self.name = json_object['name']
        self.agent_type = json_object['agentType']
        self.description = json_object['description']
        self.number_of_nodes = json_object['numberOfNodes']
        self.type = json_object['name']

        self.raw = json_object
        
        self.api = api

    @staticmethod
    def build_from_json(json_object, operation):
        return Tier(json_object, operation.api)

    def __str__(self):
        return 'Tier ID: {}\t NAME: {}'.format(self.tier_id, self.name)

