class User:

    def __init__(self, username, id):
        self.username = username
        self.id = id
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1

user_1 = User("angela","001")
user_2 = User("jack","002")

print(user_1.followers)
print(user_2.following)
user_2.follow(user_1)
print(user_1.followers)
print(user_2.following)