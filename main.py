from book import *
from student import *
from library import *

library = Library("KITABXANA")

library.addBook(Book(1, "Clean Code", "Robert Martin", 464))
library.addBook(Book(2, "Python Crash Course", "Eric Matthes", 560))
library.addBook(Book(3, "Atomic Habits", "James Clear", 320))

while True:
    print("""
1. Telebe eleave et
2. Kitablara bax
3. Kitab gotur
4. Kitab qaytar
5. Cix
""")
    choice = input("Seciminizi daxil edin ")

    if choice == "1":
        studentID = int(input("Student ID: "))
        name = input("Name: ")
        library.addStudent(Student(studentID, name))

    elif choice == "2":
        library.showBooks()

    elif choice == "3":
        studentID = int(input("Student ID: "))
        bookID = int(input("Book ID: "))
        library.borrowBook(studentID, bookID)

    elif choice == "4":
        studentID = int(input("Student ID: "))
        bookID = int(input("Book ID: "))
        library.returnBook(studentID, bookID)

    elif choice == "5":
        break