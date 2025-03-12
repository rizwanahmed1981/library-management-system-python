from admin_functions import *
from user_functions import *

id:str = input("please enter your user name: ").lower()
password:str = input("please enter your password: ").lower()

if id == "rizwan ahmed" and password == "123456":
    print("🎉Welcome Admin 🙂🙂")
    admin_funct()
elif id == "ahmed" and password == "124578":
    print(f"welcome {id}")
    user_function()