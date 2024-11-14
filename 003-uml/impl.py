from datetime import date
from dateutil.parser import parse as parse_datetime

def parse_date(source: str) -> date:
    return parse_datetime(source).date()

class Reader:
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email

    def __str__(self) -> str:
        return f"Reader '{self.name}', e-mail: {self.email}\n"

    def get_name(self) -> str:
        return self.name

    def get_email(self) -> str:
        return self.email

class Book:
    def __init__(self, name: str, author: str, genre: str, release_date: date, isbn: str):
        self.name = name
        self.author = author
        self.genre = genre
        self.release_date = release_date
        self.isbn = isbn
        self.borrowed = False
        self.borrowed_by = None
        self.borrowed_until = None
        self.waitlist = []

    def __str__(self) -> str:
        return f"Book '{self.name}' by {self.author}, genre: {self.genre}, release date: {self.release_date.strftime("%d. %m. %Y")}, ISBN: {self.isbn}, is borrowed: {f"yes, by {self.borrowed_by} until {self.borrowed_until}" if self.borrowed else "no"}\n"

    def get_name(self) -> str:
        return self.name

    def get_author(self) -> str:
        return self.author

    def get_genre(self) -> str:
        return self.genre

    def get_release_date(self) -> date:
        return self.release_date

    def get_isbn(self) -> str:
        return self.isbn

    def is_borrowed(self) -> bool:
        return self.borrowed

    def borrow(self, reader: Reader, until: date):
        if self.borrowed:
            raise Exception("Already borrowed")
        if date.today() >= until:
            raise Exception("Invalid date")
        if self.waitlist:
            if len(self.waitlist) != 1 or self.waitlist[0] != reader:
                raise Exception("Reader is not first on the waitlist")
            else:
                self.waitlist.pop(0)
        self.borrowed = True
        self.borrowed_by = reader
        self.borrowed_until = until

    def extend_borrow(self, reader: Reader, until: date):
        if not self.borrowed:
            raise Exception("Not borrowed")
        if self.borrowed_by != reader:
            raise Exception("Borrowed by different reader")
        if self.borrowed_until >= until:
            raise Exception("Invalid date")
        self.borrowed_until = until

    def return_borrowed(self, reader: Reader):
        if not self.borrowed:
            raise Exception("Not borrowed")
        if self.borrowed_by != reader:
            raise Exception("Borrowed by different reader")
        self.borrowed = False
        self.borrowed_by = None
        self.borrowed_until = None
        next_reader = self.waitlist[0]
        print(f"Sending e-mail to {next_reader.name} at {next_reader.email} that the book '{self.name}' by {self.author} is available\n")

    def add_to_waitlist(self, reader: Reader):
        self.waitlist.append(reader)

    def borrow_or_add_to_waitlist(self, reader: Reader, until: date) -> bool:
        try:
            self.borrow(reader, until)
            return True
        except:
            self.add_to_waitlist(reader)
            return False

class Catalog:
    def __init__(self, books: list[Book] = []):
        self.books = books

    def __str__(self) -> str:
        return "Catalog:\n" + "".join(map(lambda book: book.__str__(), self.books))

    def get_books(self) -> list[Book]:
        return self.books

    def add_book(self, book: Book):
        self.books.append(book)

    def remove_book(self, book: Book):
        self.books.remove(book)

    def search_by_name(self, name: str):
        return Catalog(filter(lambda book: book.name == name, self.books))

    def search_by_author(self, author: str):
        return Catalog(filter(lambda book: book.author == author, self.books))

    def search_by_genre(self, genre: str):
        return Catalog(filter(lambda book: book.genre == genre, self.books))

    def search_by_release_date(self, release_date: str):
        return Catalog(filter(lambda book: book.release_date == release_date, self.books))

    def search_by_isbn(self, isbn: str):
        return Catalog(filter(lambda book: book.isbn == isbn, self.books))

class Librarian:
    def __init__(self, name: str, catalog: Catalog, readers: list[Reader] = []):
        self.name = name
        self.catalog = catalog
        self.readers = readers

    def __str__(self) -> str:
        return "Librarian:\n" + self.catalog.__str__() + "Readers:\n" + "".join(map(lambda reader: reader.__str__(), self.readers))

    def get_name(self) -> str:
        return self.name

    def add_reader(self, reader: Reader):
        self.readers.append(reader)

    def remove_reader(self, reader: Reader):
        self.readers.remove(reader)

    # def report(self) -> str:
    #     return self.__str__()

def test():
    catalog = Catalog()

    book1 = Book("The Whispers of Elaria", "Armand Greyson", "fantasy", parse_date("March 12 2020"), "978-1-56789-123-4")
    book2 = Book("Echoes of the Past", "Lillian Harper", "fiction", parse_date("September 8 2018"), "978-1-23456-789-0")
    book3 = Book("The Quantum Paradox", "Dr. Nathaniel Cho", "fiction", parse_date("January 17 2022"), "978-1-98765-432-1")

    catalog.add_book(book1)
    catalog.add_book(book2)
    catalog.add_book(book3)

    print(catalog)

    print(catalog.search_by_name("The Whispers of Elaria"))
    print(catalog.search_by_genre("fiction"))

    librarian = Librarian("John Doe", catalog)

    reader1 = Reader("Steve", "steve@example.com")
    reader2 = Reader("Alex", "alex@example.com")

    librarian.add_reader(reader1)
    librarian.add_reader(reader2)

    success1 = book1.borrow_or_add_to_waitlist(reader2, parse_date("December 3 2024"))
    success2 = book1.borrow_or_add_to_waitlist(reader1, parse_date("November 27 2024"))

    print(librarian)

    if success1:
        book1.extend_borrow(reader2, parse_date("December 18 2024"))
        book1.return_borrowed(reader2)

    if not success2:
        book1.borrow_or_add_to_waitlist(reader1, parse_date("November 27 2024"))

    print(librarian)

def interface1():
    catalog = Catalog()
    librarian = Librarian("John Doe", catalog)

    while True:
        print("Library Menu:")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. View All Books")
        print("4. Add Reader")
        print("5. Remove Reader")
        print("6. View All Readers")
        print("7. Borrow Book")
        print("8. Return Book")
        print("9. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter book name: ")
            author = input("Enter author name: ")
            genre = input("Enter genre: ")
            release_date = parse_date(input("Enter release date (e.g., 'March 12 2020'): "))
            isbn = input("Enter ISBN: ")
            print()
            book = Book(name, author, genre, release_date, isbn)
            catalog.add_book(book)
            print(f"Book '{name}' added successfully!")

        elif choice == "2":
            name = input("Enter book name to remove: ")
            print()
            book_list = catalog.search_by_name(name).get_books()
            if book_list:
                catalog.remove_book(book_list[0])
                print(f"Book '{name}' removed successfully!")
            else:
                print("Book not found.")

        elif choice == "3":
            print()
            print(catalog)

        elif choice == "4":
            reader_name = input("Enter reader name: ")
            email = input("Enter reader email: ")
            print()
            reader = Reader(reader_name, email)
            librarian.add_reader(reader)
            print(f"Reader '{reader_name}' added successfully!")

        elif choice == "5":
            reader_name = input("Enter reader name to remove: ")
            print()
            reader_list = [reader for reader in librarian.readers if reader.get_name() == reader_name]
            if reader_list:
                librarian.remove_reader(reader_list[0])
                print(f"Reader '{reader_name}' removed successfully!")
            else:
                print("Reader not found.")

        elif choice == "6":
            print("\nReaders List:")
            for reader in librarian.readers:
                print(reader)

        elif choice == "7":
            book_name = input("Enter book name to borrow: ")
            reader_name = input("Enter reader name: ")
            until_date = parse_date(input("Enter return date (e.g., 'December 3 2024'): "))
            print()
            book_list = catalog.search_by_name(book_name).get_books()
            reader_list = [reader for reader in librarian.readers if reader.get_name() == reader_name]

            if book_list and reader_list:
                book = book_list[0]
                reader = reader_list[0]
                success = book.borrow_or_add_to_waitlist(reader, until_date)
                if success:
                    print(f"Book '{book_name}' borrowed by {reader_name} until {until_date}.")
                else:
                    print(f"Book '{book_name}' is already borrowed. Added {reader_name} to the waitlist.")
            else:
                print("Book or reader not found.")

        elif choice == "8":
            book_name = input("Enter book name to return: ")
            reader_name = input("Enter reader name: ")
            print()
            book_list = catalog.search_by_name(book_name).get_books()
            reader_list = [reader for reader in librarian.readers if reader.get_name() == reader_name]

            if book_list and reader_list:
                book = book_list[0]
                reader = reader_list[0]
                try:
                    book.return_borrowed(reader)
                    print(f"Book '{book_name}' returned successfully by {reader_name}.")
                except Exception as e:
                    print(f"Error: {e}")
            else:
                print("Book or reader not found.")

        elif choice == "9":
            print("Exiting library system. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

def interface2():
    catalog = Catalog()

    book1 = Book("The Whispers of Elaria", "Armand Greyson", "fantasy", parse_date("March 12 2020"), "978-1-56789-123-4")
    book2 = Book("Echoes of the Past", "Lillian Harper", "fiction", parse_date("September 8 2018"), "978-1-23456-789-0")
    book3 = Book("The Quantum Paradox", "Dr. Nathaniel Cho", "fiction", parse_date("January 17 2022"), "978-1-98765-432-1")
    catalog.add_book(book1)
    catalog.add_book(book2)
    catalog.add_book(book3)

    librarian = Librarian("John Doe", catalog)

    while True:
        print("Welcome to the Library System")
        user_type = input("Login as (librarian/reader): ").strip().lower()

        if user_type == "librarian":
            print(f"Logged in as Librarian: {librarian.get_name()}")
            while True:
                print("\nLibrarian Options:")
                print("1. Add a book")
                print("2. Remove a book")
                print("3. Add a reader")
                print("4. Remove a reader")
                print("5. List all readers")
                print("6. List all books")
                print("7. Logout")
                choice = input("Choose an option: ").strip()

                if choice == "1":
                    name = input("Enter book name: ")
                    author = input("Enter author: ")
                    genre = input("Enter genre: ")
                    release_date = parse_date(input("Enter release date (e.g., March 12 2020): "))
                    isbn = input("Enter ISBN: ")
                    book = Book(name, author, genre, release_date, isbn)
                    librarian.catalog.add_book(book)
                    print(f"Book '{name}' added successfully!")

                elif choice == "2":
                    book_name = input("Enter the name of the book to remove: ")
                    book_to_remove = next((book for book in librarian.catalog.get_books() if book.get_name() == book_name), None)
                    if book_to_remove:
                        librarian.catalog.remove_book(book_to_remove)
                        print(f"Book '{book_name}' removed successfully!")
                    else:
                        print("Book not found.")

                elif choice == "3":
                    reader_name = input("Enter reader name: ")
                    reader_email = input("Enter reader email: ")
                    reader = Reader(reader_name, reader_email)
                    librarian.add_reader(reader)
                    print(f"Reader '{reader_name}' added successfully!")

                elif choice == "4":
                    reader_name = input("Enter the name of the reader to remove: ")
                    reader_to_remove = next((reader for reader in librarian.readers if reader.get_name() == reader_name), None)
                    if reader_to_remove:
                        librarian.remove_reader(reader_to_remove)
                        print(f"Reader '{reader_name}' removed successfully!")
                    else:
                        print("Reader not found.")

                elif choice == "5":
                    print("List of Readers:")
                    for reader in librarian.readers:
                        print(reader)

                elif choice == "6":
                    print(librarian.catalog)

                elif choice == "7":
                    break

                else:
                    print("Invalid option, please try again.")

        elif user_type == "reader":
            reader_name = input("Enter your name: ").strip()
            reader = next((r for r in librarian.readers if r.get_name() == reader_name), None)
            if reader:
                print(f"Welcome {reader.get_name()}")
                while True:
                    print("\nReader Options:")
                    print("1. Borrow a book")
                    print("2. Return a book")
                    print("3. List available books")
                    print("4. Logout")
                    choice = input("Choose an option: ").strip()

                    if choice == "1":
                        book_name = input("Enter the name of the book to borrow: ")
                        book = next((b for b in librarian.catalog.get_books() if b.get_name() == book_name), None)
                        if book:
                            until_date = parse_date(input("Enter the return date (e.g., December 3 2024): "))
                            if book.borrow_or_add_to_waitlist(reader, until_date):
                                print(f"You have successfully borrowed '{book_name}'.")
                            else:
                                print(f"'{book_name}' is currently borrowed. You have been added to the waitlist.")
                        else:
                            print("Book not found.")

                    elif choice == "2":
                        book_name = input("Enter the name of the book to return: ")
                        book = next((b for b in librarian.catalog.get_books() if b.get_name() == book_name), None)
                        if book:
                            try:
                                book.return_borrowed(reader)
                                print(f"You have successfully returned '{book_name}'.")
                            except Exception as e:
                                print(f"Error: {e}")
                        else:
                            print("Book not found.")

                    elif choice == "3":
                        print("Available Books:")
                        for book in librarian.catalog.get_books():
                            if not book.is_borrowed():
                                print(book)

                    elif choice == "4":
                        break

                    else:
                        print("Invalid option, please try again.")
            else:
                print("Reader not found. Please contact the librarian to register.")
        else:
            print("Invalid user type. Please enter 'librarian' or 'reader'.")

if __name__ == "__main__":
    # test()
    # interface1()
    interface2()
