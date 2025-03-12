from admin_functions import admin_funct
from user_functions import user_function
from users import users

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

        


    
# for id in range(users):
#     for password in users[id]:
#         if id == "admin" and password == "123456":
#             print("🎉Welcome Admin 🙂🙂")
#             admin_funct()
#         elif id == "user1" and password == "124578":
#             print(f"welcome back {id}")
#             user_function()
        