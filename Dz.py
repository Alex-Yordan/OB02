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

    def add_user_name(self, user):
            self._users.append(user)
            print(f"Пользователь {user.get_user_name()} добавлен в систему.")

    def remove_user_name(self, user):
            self._users.remove(user)
            print(f"Пользователь {user.get_user_name()} удален из системы.")

    def get_users(self):

        return [user.get_user_name() for user in self._users]


users = []
user1 = User("40020", "Uriy")
user2 = User("40030", "Ulia")
admin = Admin("100", "MAX",)

admin.add_user_name(user1)
admin.add_user_name(user2)
print("Список пользователей:", admin.get_users())

admin.remove_user_name(user1)
print("Список пользователей:", admin.get_users())
