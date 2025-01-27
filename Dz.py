class User():
    def __init__(self, ID, name, access):

        self._ID = ID
        self._user_name = name
        self._access = access

class Admin(User):
    def __init__(self, add_user, rem_user):
        super().__init__()




user1 = User("40020", "Uriy", "5")
user2 = User("40030", "Ulia", "2")
admin1 = Admin("100", "", "5")