import json
import os

# creating a dictionary of user books
user_books: dict = {
    "The Great Gatsby": {
        "date": "15-3-2025",
        "read_percentage": "25%"
    },
    "To Kill a Mockingbird":{
        "date": "15-3-2025",
        "read_percentage": "40%"
    },
    
}

# user adding books of his collection to JSON file
def save_user_books():
    """this function will save user borrowed books into a json file"""
    with open("user_books.json", "w") as file:
        json.dump(user_books, file, indent=4)
        
# save_user_books()

# looding JSON file
def load_user_books():
    """this function will load user borrowed books from json file"""
    if os.path.exists("user_books.json"):
        with open("user_books.json", "r") as file:
            return json.load(file)
        
    return {}

user_books = load_user_books()

# print(user_books)
"""
new_user_book = input("please enter book name to borrow: ")
date = input("Enter today's date: ")
percentage_read = input("what percentage you have read this book today: ")

user_books[new_user_book]= {
    "date" : date,
    "read_percentage": percentage_read
}
save_user_books()
"""
# print(user_books)