# helper.py
import json
from icecream import ic

LIBRARY_FILE = 'library.json'

def load_data():
    try:
        with open(LIBRARY_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {"books": [], "borrowers": [], "borrowed_books": []}

def save_data(data):
    with open(LIBRARY_FILE, 'w') as file:
        json.dump(data, file, indent=4)

def view_books():
    data = load_data()
    ic(data['books'])
    if data['books']:
        for book in data['books']:
            print(f"ID: {book['id']}, Title: {book['title']}, Author: {book['author']}")
    else:
        print("No books available.")

def view_borrowers():
    data = load_data()
    ic(data['borrowers'])
    if data['borrowers']:
        for borrower in data['borrowers']:
            print(f"ID: {borrower['id']}, Name: {borrower['first_name']} {borrower['last_name']}, Phone: {borrower['phone_num']}, Email: {borrower['email']}")
    else:
        print("No borrowers.")

def borrow_book():
    data = load_data()
    book_id = input("Enter book ID to borrow: ")
    borrower_id = input("Enter your ID: ")
    
    book = next((b for b in data['books'] if b['id'] == book_id), None)
    if book:
        data['borrowed_books'].append({"book_id": book_id, "borrower_id": borrower_id})
        save_data(data)
        print("Book borrowed successfully.")
    else:
        print("Book not found.")

def view_borrowed_books():
    data = load_data()
    ic(data['borrowed_books'])
    if data['borrowed_books']:
        for borrowed in data['borrowed_books']:
            book = next((b for b in data['books'] if b['id'] == borrowed['book_id']), None)
            borrower = next((b for b in data['borrowers'] if b['id'] == borrowed['borrower_id']), None)
            print(f"Book ID: {book['id']}, Title: {book['title']}, Borrower: {borrower['first_name']} {borrower['last_name']}")
    else:
        print("No borrowed books.")

def return_book():
    data = load_data()
    book_id = input("Enter book ID to return: ")
    borrowed_book = next((b for b in data['borrowed_books'] if b['book_id'] == book_id), None)
    
    if borrowed_book:
        data['borrowed_books'].remove(borrowed_book)
        save_data(data)
        print("Book returned successfully.")
    else:
        print("Borrowed book not found.")

def sign_up_borrower():
    data = load_data()
    
    new_borrower = {
        "id": input("Enter ID: "),
        "first_name": input("Enter first name: "),
        "last_name": input("Enter last name: "),
        "phone_num": input("Enter phone number: "),
        "email": input("Enter email: ")
    }
    
    data['borrowers'].append(new_borrower)
    save_data(data)
    print("New borrower signed up successfully.")

def add_new_book():
    data = load_data()
    
    new_book = {
        "id": input("Enter book ID: "),
        "title": input("Enter book title: "),
        "author": input("Enter book author: ")
    }
    
    data['books'].append(new_book)
    save_data(data)
    print("New book added successfully.")
