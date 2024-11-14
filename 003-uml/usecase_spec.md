# Actors:

Reader: An individual who interacts with the library system to manage book-related activities.
Librarian: A system administrator responsible for maintaining the library system and managing user data.

# Use Cases:

## 1. UC1: Lookup a book

Actor: Reader
Description: The Reader searches for a book in the library catalog to check its availability or details.

## 2. UC2: Borrow a book

Actor: Reader
Description: The Reader borrows an available book from the library.

## 3. UC3: Return a book

Actor: Reader
Description: The Reader returns a previously borrowed book to the library. Next reader on the waitlist is automatically verified.

## 4. UC4: Make a book reservation

Actor: Reader
Description: The Reader reserves a book that is currently not available.

## 5. UC5: Extend the time of borrowing

Actor: Reader
Description: The Reader extends the borrowing period for a book they have checked out.

## 6. UC6: Add a book to the system

Actor: Librarian
Description: The Librarian adds new book information to the library system.

## 7. UC7: Report generation

Actor: Librarian
Description: The Librarian generates reports for library management purposes.

## 8. UC8: User Administration

Actor: Librarian
Description: The Librarian manages user accounts (e.g., creating, updating, or deleting accounts).
