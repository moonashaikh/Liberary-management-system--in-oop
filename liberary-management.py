import sys

class Library:
    def __init__(self, listofbooks):
        self.availablebooks = listofbooks

    def displayAvailablebooks(self):
        print("\nThe books we have in our Library are:")
        for book in self.availablebooks:
            print(f"- {book}")

    def lendBook(self, requestedBook):
        if requestedBook in self.availablebooks:
            print(f"You have now borrowed: {requestedBook}")
            self.availablebooks.remove(requestedBook)
        else:
            print("Sorry, it's not in the Library.")

    def addBook(self, returnedBook):
        self.availablebooks.append(returnedBook)
        print(f"Thanks for returning: {returnedBook}")


class Student:
    def requestBook(self):
        book = input("Enter the name of the book you'd like to check out: ")
        return book

    def returnBook(self):
        book = input("Enter the name of the book you'd like to return: ")
        return book


def main():
    library = Library(["The Last Battle", "The Great Divorce", "Chemistry book"])
    student = Student()

    while True:
        print("""
------- LIBRARY MENU -------
1. Display all available books
2. Request a book
3. Return a book 
4. Exit 
""")
        try:
            choice = int(input("Enter your choice (1-4): "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice == 1:
            library.displayAvailablebooks()
        elif choice == 2:
            library.lendBook(student.requestBook())
        elif choice == 3:
            library.addBook(student.returnBook())
        elif choice == 4:
            print("Thanks for using the library. Goodbye!")
            sys.exit()
        else:
            print("Invalid choice. Please select between 1 and 4.")

# Call main function
main()
