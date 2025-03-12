import json
import os

users = {
    "admin": {"password": "123456"},
    "user1": {"password": "124578"},
    "user2": {"password": "784512"},
    "user3": {"password": "456789"}
}


def save_user():
    with open("user.json", "w") as file:
        json.dump(users, file, indent=4)
        
# save_user()

def load_user():
    """Loads the users from json file"""
    if os.path.exists("user.json"):
        with open("user.json", "r") as file:
            return json.load(file)
    
    return {}

users = load_user()
# print(users)


