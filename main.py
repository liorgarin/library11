import json
from enum import Enum
from icecream import ic
import helper

class MenuOptions(Enum):
    VIEW_BOOKS = 1
    VIEW_BORROWERS = 2
    BORROW_BOOK = 3
    VIEW_BORROWED_BOOKS = 4
    RETURN_BOOK = 5
    SIGN_UP_BORROWER = 6
    ADD_NEW_BOOK = 7
    EXIT = 8

def main():
    while True:
        print_menu()
        try:
            choice = int(input("Enter your choice: "))
            ic(choice)
            
            if choice == MenuOptions.VIEW_BOOKS.value:
                helper.view_books()
            elif choice == MenuOptions.VIEW_BORROWERS.value:
                helper.view_borrowers()
            elif choice == MenuOptions.BORROW_BOOK.value:
                helper.borrow_book()
            elif choice == MenuOptions.VIEW_BORROWED_BOOKS.value:
                helper.view_borrowed_books()
            elif choice == MenuOptions.RETURN_BOOK.value:
                helper.return_book()
            elif choice == MenuOptions.SIGN_UP_BORROWER.value:
                helper.sign_up_borrower()
            elif choice == MenuOptions.ADD_NEW_BOOK.value:
                helper.add_new_book()
            elif choice == MenuOptions.EXIT.value:
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def print_menu():
    print("Library Menu:")
    for option in MenuOptions:
        print(f"{option.value}. {option.name.replace('_', ' ').title()}")

if __name__ == "__main__":
    main()
