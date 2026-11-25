# 📚 Library Management System

A simple console application written in Python using OOP (object-oriented programming). You can add students, view books, borrow books, and return them.

## Features

- Add students to the library
- View all books and their status (available / borrowed)
- Borrow a book as a student
- Return a borrowed book
- Warning messages when a book is already borrowed or a student/book is not found

## Project Structure

```
OP/
├── book.py       # Book class
├── student.py    # Student class
├── library.py    # Library class
├── main.py       # Main menu (entry point)
└── README.md
```

## Classes

| File | Class | Description |
|------|-------|-------------|
| `book.py` | `Book` | Stores the book's ID, title, author, page count, and availability status. Has `borrow()` and `returnBook()` methods. |
| `student.py` | `Student` | Stores the student's ID, name, and the list of borrowed books (`borrowedBooks`). |
| `library.py` | `Library` | Manages the lists of books and students. Handles adding, searching, borrowing, and returning. |

### Library Methods

- `addBook(book)` – adds a book
-
