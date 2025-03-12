from inventory import *
from users import *
from user_books import *

# user functionality

def user_function():
    print(f"""select
          1: To borrow new book
          2: for your books collection
          3: for returning book
          4: check for available books in labrary
          5: search book in library
          6: search book in your collection
          0: to Quit""")
    user_input = input("What do you want to do today: ").lower()
    if user_input == "1":
        borrow_book()
    elif user_input == "2":
        user_inventory()
    elif user_input == "3":
        return_book()
    elif user_input == "4":
        inventory()
    elif user_input == "5":
        search_book_in_library()
    elif user_input == "6":
        search_book_in_collection()
    elif user_input == "0":
        print("thank you for using our library, do visit again 🙂🙂")
        exit()
    else:
        print("⛔ inavlaid choice please select right number: ")
        user_function()

# user_function()

# user borrowing books to his/ her collection
def borrow_book():
    new_user_book = input("please enter book name to borrow: ")
    date = input("Enter today's date: ")
    percentage_read = input("what percentage you have read this book today: ")

    user_books[new_user_book]= {
        "date" : date,
        "read_percentage": percentage_read
    }
    save_user_books()
    print(f"✔ new book {new_user_book} added to your collection:  ")
    print("=================================================")
    user_input2 = input("Do you want to do anything else here? YES / NO: ").lower()
    if user_input2 == "yes":
        user_function()
    else:
        print("Thank you for using our library, do visit again 🙂🙂")
        exit()
      
      
# user's books collection
def user_inventory():
    print(user_books)
    print("=================================================")
    user_input2 = input("Do you want to do anything else here? YES / NO: ").lower()
    if user_input2 == "yes":
        user_function()
    else:
        print("Thank you for using our library, do visit again 🙂🙂")
        exit()
        
        
# user returning books to library
def return_book():
    book_name = input("Enter name of the book you want to return: ")
    if book_name in user_books:
        del user_books[book_name]
        print(f"✔book {book_name} returned to library")
        print("=================================================")
        user_input2 = input("Do you want to do anything else here? YES / NO: ").lower()
        if user_input2 == "yes":
            user_function()
        else:
            print("Thank you for using our library, do visit again 🙂🙂")
            exit()
    else:
        print(f"❌ {book_name} does not exists in your collection")
        print("please select from your bellow collection")
        print(user_books)
        return_book()
    
# collection of books in library
def inventory():
    print(books)
    print("=================================================")
    user_input2 = input("Do you want to do anything else here? YES / NO: ").lower()
    if user_input2 == "yes":
        user_function()
    else:
        print("Thank you for using our library, do visit again 🙂🙂")
        exit()


def search_book_in_library():
    title = input("Enter title of book to 🔎: ")
    if title in books:
        print("matching book found ✔")
        print(f"""{title.upper()} by {books[title]["author"]} ({books[title]["publication_year"]}) - {books[title]["genre"]} book exists""")
        print("=================================================")
        user_input2 = input("Do you want to do anything else here? YES / NO: ").lower()
        if user_input2 == "yes":
            user_function()
        else:
            print("Thank you for using our library, do visit again 🙂🙂")
            exit()
    else:
        print(f"⛔ {title.title()} does not exists in library")
        print("=================================================")
        user_input2 = input("Do you want to do anything else here? YES / NO: ").lower()
        if user_input2 == "yes":
            user_function()
        else:
            print("Thank you for using our library, do visit again 🙂🙂")
            exit()


def search_book_in_collection():
    title = input("please enter title of the book to 🔎: ")
    if title in user_books:
        print("matching book found ✔")
        print(f"""{title.upper()} borrowed at {user_books[title]["date"]} and completed {user_books[title]["read_percentage"]}""")
        print("=================================================")
        user_input2 = input("Do you want to do anything else here? YES / NO: ").lower()
        if user_input2 == "yes":
            user_function()
        else:
            print("Thank you for using our library, do visit again 🙂🙂")
            exit()
    else:
        print(f"""⛔ {title.title()} does not exists in your collection""")
        print("=================================================")
        user_input2 = input("Do you want to do anything else here? YES / NO: ").lower()
        if user_input2 == "yes":
            user_function()
        else:
            print("Thank you for using our library, do visit again 🙂🙂")
            exit()
    
# search_book_in_collection()
# search_book_in_library()
# calling user function
# user_function()