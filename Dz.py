class User():
    def __init__(self, ID, name):

        self._ID = ID
        self._user_name = name
        self._access = "user"

    def get_ID(self):
        return self._ID

    def get_user_name(self):
        return self._user_name

    def get_access(self):
        return self._access

    def set_name(self, name):
        self._user_name = name

class Admin(User):
    def __init__(self, ID, name):
        super().__init__(ID, name)
        self._access = 'admin'
        self._users = []

        def add_user(self, User):

        def remove_user(self, user)
            




user1 = User("40020", "Uriy", "5")
user2 = User("40030", "Ulia", "2")
admin1 = Admin("100", "", "5")