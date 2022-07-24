class Users():
    def __init__(self, user_id, username):
        self.id = user_id
        self.name = username


u_name = input("Enter Your name: ")
user_1 = Users("001", u_name)

print(user_1.name)