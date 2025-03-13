from inventory import *
from users import *

# Admin functionality

def admin_funct():
    print(f"""please select
          1: Add book
          2: update book
          3: delete book
          4: Veiw inventory
          5: add user
          6: delete user
          7: for user list
          8: search a book in library
          0: Quit""")
    admin_input = input("what do you want to do? ")
    
    if admin_input == "1":
        add_book()
    elif admin_input == "2":
        book_name = input("Enter name of book to update: ")
        update_book(book_name)
    elif admin_input == "3":
        book_name = input("Enter name of book to delete: ")
        delete_book(book_name)
    elif admin_input == "4":
        veiw_inventory()
    elif admin_input == "5":
        user_name = input("Enter new user name: ").lower()
        user_password = input("Enter user password: ").lower()
        add_new_user(user_name, user_password)
    elif admin_input == "6":
        user_name = input("Enter user name to delete: ").lower()
        delete_user(user_name)
    elif admin_input == "7":
        user_list()
    elif admin_input == "8":
        search_in_library()
    elif admin_input == "0":
        print("Thank You Admin have a Nice Day 😊 ")
        exit()
    else:
        print("invalid input! please choose a correct option")
        admin_funct()
        
# book addition function
def add_book():
    new_book = input("please enter book name: ")
    author = input("please enter author name: ")
    publication_year = input("please enter publication year: ")
    genre = input("please enter genre: ")

    books[new_book] = {
        "author": author,
        "publication_year": publication_year,
        "genre": genre
    }

    save_book()
    print(f"✔ Book added: {new_book}")
    
    print("=====================================================")
    admin_function_recal()


# book updation function
def update_book(book_name):
    if book_name in books:
               
        new_book = book_name
        author = input("please enter author name: ")
        publication_year = input("please enter publication year: ")
        genre = input("please enter genre: ")

        books[new_book] = {
            "author": author,
            "publication_year": publication_year,
            "genre": genre
        }

        save_book()
        print(f"✔ Book updated: {new_book}")
        print("=====================================================")
        admin_function_recal()
    else:
        print(f"❌ book name {book_name} not found!")
        print("=====================================================")
        admin_function_recal()

# book delete function    
def delete_book(book_name):
    if book_name in books:
        del books[book_name]
        save_book()
        print(f"✔ {book_name} deleted")
    else:
        print(f"❌ book name {book_name} not found!")
    print("=====================================================")
    admin_function_recal()

# inventory veiw function
def veiw_inventory():
    print(books)
    print("=====================================================")
    admin_function_recal()


# user addition function by admin
def add_new_user(user_name, user_password):
    if user_name in users:
        print("⛔ user already exists: ")
    else:
        users[user_name] = {
            "password": user_password
        }
        save_user()
    print(f"✔new user {user_name} added")
    print("=====================================================")
    admin_function_recal()
        
        
# user deletion function by admin
def delete_user(user_name):
    if user_name in users:
        del users[user_name]
        save_user()
        print(f"✔user account named {user_name} deleted permanentely!")
    else:
        print(f"❌ user account name {user_name} not found")
    print("=====================================================")
    admin_function_recal()
        
def user_list():
    print(users)
    admin_function_recal()
        

def search_in_library():
    title = input("Enter title of book: ")
    if title in books:
        print("matching book found ✔")
        print(f"""{title.upper()} by {books[title]["author"]} ({books[title]["publication_year"]}) - {books[title]["genre"]} book exists""")
        print("=================================================")
        admin_function_recal()
    else:
        print(f"⛔ {title.title()} does not exists in library")
        print("=================================================")
        admin_function_recal()
            
            
def admin_function_recal():
    admin_input2 = input("Do you want to perform anything else Yes/ No: ").lower()
    if admin_input2 == "yes":
        admin_funct()
    else:
        print("Thank You Admin have a Nice Day 😊 ")
        exit()