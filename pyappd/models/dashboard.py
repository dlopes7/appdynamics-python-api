

class Dashboard():
    def __init__(self, json_object):
        self.raw = json_object
        self.modified_on = json_object['modifiedOn']
        self.created_by = json_object['createdBy']
        self.color = json_object['color']
        self.name_unique = json_object['nameUnique']
        self.missing_associated_entities = json_object['missingAssociatedEntities']
        self.height = json_object['height']
        self.disabled = json_object['disabled']
        self.layout_type = json_object['layoutType']
        self.war_room = json_object['warRoom']
        self.id = json_object['id']
        self.description = json_object['description']
        self.width = json_object['width']
        self.version = json_object['version']
        self.modified_by = json_object['modifiedBy']
        self.background_color = json_object['backgroundColor']
        self.widgets = json_object['widgets']
        self.template_entity_type = json_object['templateEntityType']
        self.template = json_object['template']
        self.built_in = json_object['builtIn']
        self.start_time = json_object['startTime']
        self.sharing_revoked = json_object['sharingRevoked']
        self.security_token = json_object['securityToken']
        self.properties = json_object['properties']
        self.name = json_object['name']
        self.canvas_type = json_object['canvasType']
        self.created_on = json_object['createdOn']
        self.minutes_before_anchor_time = json_object['minutesBeforeAnchorTime']
        self.refresh_interval = json_object['refreshInterval']
        self.end_time = json_object['endTime']

    @staticmethod
    def build_from_json(json_object, operation):
        return Dashboard(json_object)

    def __str__(self):
        return '{}'.format(self.name)
