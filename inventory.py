import json
import os

books: dict = {
    "The Great Gatsby": {
        "author": "F. Scott Fitzgerald",
        "publication_year": 1925,
        "genre": "Fiction"
    },
    "1984": {
        "author": "George Orwell",
        "publication_year": 1949,
        "genre": "Dystopian"
    },
    "To Kill a Mockingbird": {
        "author": "Harper Lee",
        "publication_year": 1960,
        "genre": "Fiction"
    },
    "The Catcher in the Rye": {
        "author": "J.D. Salinger",
        "publication_year": 1951,
        "genre": "Fiction"
    },
    "The Lord of the Rings": {
        "author": "J.R.R. Tolkien",
        "publication_year": 1954,
        "genre": "Fantasy"
    },
    "Pride and Prejudice": {
        "author": "Jane Austen",
        "publication_year": 1813,
        "genre": "Romance"
    },
    "The Alchemist": {
        "author": "Paulo Coelho",
        "publication_year": 1988,
        "genre": "Adventure, Fantasy"
    },
    "Moby-Dick": {
        "author": "Herman Melville",
        "publication_year": 1851,
        "genre": "Adventure"
    }
}



def save_book():
    """Save the Book dictionary to json file"""
    with open("books.json", "w") as file:
        json.dump(books, file, indent=4)

# save_book()



def load_books():
    """Loads the books dictionary from json file if it exists"""
    if os.path.exists("books.json"):
        with open("books.json", "r") as file:
            return json.load(file)
        
    return {} # returns an empty dictionary if file doesnt exists
books = load_books()
# print(books)

"""
new_book = input("please enter book name: ")
author = input("please enter author name: ")
publication_year = input("please enter publication year: ")
genre = input("please enter genre: ")

books[new_book] = {
    "author": author,
    "publication_year": publication_year,
    "genre": genre
}

# save_book()
"""

# print(books)


# books.update({"adeel":{"author": "rizwan", "publication_year": 2025, "genre":"person"}})
# print(books)

# print("=====================================")
# del books["1984"]

# print(books)