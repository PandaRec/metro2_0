class station:
    lat = 0.0
    lng = 0.0
    name = ''
    description = ''
    id = 0
    color = ''

    def __init__(self):
        self.name = ''
        self.lat = 0.0
        self.lng = 0.0
        self.description = ''
        self.id = 0
        self.color = ''

    def set_name(self, name):
        self.name = name

    def set_id(self, id):
        self.id = id

    def set_lat(self, lat):
        self.lat = lat

    def set_lng(self, lng):
        self.lng = lng

    def set_color(self, color):
        self.color = color

    def set_description(self, description):
        self.description = description

    def get_name(self):
        return self.name

    def get_id(self):
        return self.id

    def get_lat(self):
        return self.lat

    def get_lng(self):
        return self.lng

    def get_color(self):
        return self.color

    def get_description(self):
        return self.description