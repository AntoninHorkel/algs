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

if __name__ == "__main__":
    test()
