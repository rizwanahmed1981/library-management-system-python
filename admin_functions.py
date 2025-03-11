from inventory import *
# Admin functionality

def admin_funct():
    print(f"1: Add book, 2: update book, 3: delete book, 4: Veiw inventory, 5: add user, 6: delete user 0: Quit")
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
        add_new_user()
    elif admin_input == "6":
        delete_user()
    elif admin_input == "0":
        print("Thank You Admin have a Nice Day 😊 ")
        exit()
    else:
        print("invalid input! please choose a correct option")
        print(f"1: Add book, 2: update book, 3: delete book, 4: Veiw inventory, 5: add user, 6: delete user")
        admin_input = input("what do you want to do? ")
        
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
    admin_input2 = input("Do you want to perform anything else Yes/ No: ").lower()
    if admin_input2 == "yes":
        admin_funct()
    else:
        print("Thank You Admin have a Nice Day 😊 ")
        exit()


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
        admin_input2 = input("Do you want to perform anything else Yes/ No: ").lower()
        if admin_input2 == "yes":
            admin_funct()
        else:
            print("Thank You Admin have a Nice Day 😊 ")
            exit()
    else:
        print(f"❌ book name {book_name} not found!")
        print("=====================================================")
        admin_input2 = input("Do you want to perform anything else Yes/ No: ").lower()
        if admin_input2 == "yes":
            admin_funct()
        else:
            print("Thank You Admin have a Nice Day 😊 ")
            exit()

# book delete function    
def delete_book(book_name):
    if book_name in books:
        del books[book_name]
        save_book()
        print(f"✔ {book_name} deleted")
    else:
        print(f"❌ book name {book_name} not found!")
    print("=====================================================")
    admin_input2 = input("Do you want to perform anything else Yes/ No: ").lower()
    if admin_input2 == "yes":
        admin_funct()
    else:
        print("Thank You Admin have a Nice Day 😊 ")
        exit()

# inventory veiw function
def veiw_inventory():
    print(books)
    print("=====================================================")
    admin_input2 = input("Do you want to perform anything else Yes/ No: ").lower()
    if admin_input2 == "yes":
        admin_funct()
    else:
        print("Thank You Admin have a Nice Day 😊 ")
        exit()


# user addition function by admin
def add_new_user():
    print("user added")
    print("=====================================================")
    admin_input2 = input("Do you want to perform anything else Yes/ No: ").lower()
    if admin_input2 == "yes":
        admin_funct()
    else:
        print("Thank You Admin have a Nice Day 😊 ")
        exit()
        
        
# user deletion function by admin
def delete_user():
    print("book deleted")
    print("=====================================================")
    admin_input2 = input("Do you want to perform anything else Yes/ No: ").lower()
    if admin_input2 == "yes":
        admin_funct()
    else:
        print("Thank You Admin have a Nice Day 😊 ")
        exit()