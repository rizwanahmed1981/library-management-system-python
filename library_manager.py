from admin_functions import admin_funct
from user_functions import user_function
from users import users

def login():
    while True:  # Keep asking until valid login
        username = input("Please enter your username: ").lower()
        password = input("Please enter your password: ").lower()

        # Check if user exists
        if username in users and users[username]["password"] == password:
            print(f"✅ Login Successful! Welcome back 🎉 {username.capitalize()} 🙂🙂!")

            # If user is admin, call admin function
            if username == "admin":
                admin_funct()
            else:
                user_function()
            break  # Exit loop after successful login

        else:
            print("❌ Incorrect username or password. Please try again.")

# Run the login function
login()

"""
id:str = input("please enter your user name: ").lower()
password:str = input("please enter your password: ").lower()


for id in users:
    if "admin" == id and users[id]["password"] == password:
        print("🎉 Welcome Admin 🙂🙂")
        admin_funct()
    elif "user1" == id and users[id]["password"] == password:
        print(f"Login Succesfull! Welcome back {id}!")
        user_function()
    elif "user2" == id and users[id]["password"] == password:
        print(f"Login Succesfull! Welcome back {id}!")
        user_function()
    elif "user3" == id and users[id]["password"] == password:
        print(f"Login Succesfull! Welcome back {id}!")
        user_function()
    else:
        print("user does not exists")
        exit()

        
"""

    
# for id in range(users):
#     for password in users[id]:
#         if id == "admin" and password == "123456":
#             print("🎉Welcome Admin 🙂🙂")
#             admin_funct()
#         elif id == "user1" and password == "124578":
#             print(f"welcome back {id}")
#             user_function()
        