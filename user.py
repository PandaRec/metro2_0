class current_user:
    id = 1
    login = ''
    phone = ''
    friends = []
    def __init__(self):
        self.id = 0
        self.login = ''
        self.phone = ''
        self.friends = []

    def set_id(self, id):
        self.id = id

    def set_login(self, login):
        self.login = login

    def set_phone(self, phone):
        self.phone = phone

    def set_friends(self, friends):
        self.friends = friends

    def get_id(self):
        return self.id

    def get_login(self):
        return self.login

    def get_phone(self):
        return self.phone

    def get_friends(self):
        return self.friends