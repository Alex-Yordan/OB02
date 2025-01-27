class User():
    def __init__(self, ID, name, access):

        self.name = ID
        self.voice = name
        self.color = access

class Admin(User):
    def __init__(self, add_user, rem_user):
        super().__init__("")

        self.add = add_user
        self.remove = rem_user
