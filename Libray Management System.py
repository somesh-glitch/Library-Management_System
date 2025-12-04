import sqlite3
from getpass import getpass
from datetime import datetime
import os

# ----------------------------------------------------------------
# Utility Functions
# ----------------------------------------------------------------
def clear():
    os.system("cls" if os.name == "nt" else "clear")

def timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


# ----------------------------------------------------------------
# Database Manager
# ----------------------------------------------------------------
class Database:
    def __init__(self, db_name="library.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()

    # Create all required DB tables
    def create_tables(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL,
                role TEXT NOT NULL CHECK(role IN ('admin','member'))
            )
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS books (
                book_id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                author TEXT NOT NULL,
                category TEXT NOT NULL,
                isbn TEXT NOT NULL,
                available INTEGER NOT NULL DEFAULT 1
            )
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS borrow_log (
                log_id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                book_id INTEGER,
                borrow_date TEXT,
                return_date TEXT,
                FOREIGN KEY(user_id) REFERENCES users(user_id),
                FOREIGN KEY(book_id) REFERENCES books(book_id)
            )
        """)

        self.conn.commit()

    # Insert user
    def add_user(self, name, email, password, role):
        self.cursor.execute(
            "INSERT INTO users (name, email, password, role) VALUES (?,?,?,?)",
            (name, email, password, role)
        )
        self.conn.commit()

    # Validate user login
    def authenticate(self, email, password):
        self.cursor.execute(
            "SELECT user_id, name, role FROM users WHERE email=? AND password=?",
            (email, password)
        )
        return self.cursor.fetchone()

    # Add book
    def add_book(self, title, author, category, isbn):
        self.cursor.execute(
            "INSERT INTO books (title, author, category, isbn) VALUES (?,?,?,?)",
            (title, author, category, isbn)
        )
        self.conn.commit()

    # View all books
    def get_books(self):
        self.cursor.execute("SELECT * FROM books")
        return self.cursor.fetchall()

    # Search books
    def search_books(self, keyword):
        kw = f"%{keyword}%"
        self.cursor.execute("""
            SELECT * FROM books 
            WHERE title LIKE ? OR author LIKE ? OR category LIKE ?
        """, (kw, kw, kw))
        return self.cursor.fetchall()

    # Borrow book
    def borrow_book(self, user_id, book_id):
        # Check availability
        self.cursor.execute("SELECT available FROM books WHERE book_id=?", (book_id,))
        res = self.cursor.fetchone()

        if not res:
            return "Book not found."

        if res[0] == 0:
            return "Book already issued."

        # Mark unavailable
        self.cursor.execute("UPDATE books SET available=0 WHERE book_id=?", (book_id,))
        self.cursor.execute(
            "INSERT INTO borrow_log (user_id, book_id, borrow_date) VALUES (?,?,?)",
            (user_id, book_id, timestamp())
        )
        self.conn.commit()
        return "The book has been issued successfully."

    # Return book
    def return_book(self, book_id):
        self.cursor.execute("SELECT available FROM books WHERE book_id=?", (book_id,))
        res = self.cursor.fetchone()

        if not res:
            return "Book not found."
        if res[0] == 1:
            return "Book was not issued."

        # Mark available
        self.cursor.execute("UPDATE books SET available=1 WHERE book_id=?", (book_id,))
        self.cursor.execute("""
            UPDATE borrow_log 
            SET return_date=? 
            WHERE book_id=? AND return_date IS NULL
        """, (timestamp(), book_id))

        self.conn.commit()
        return "The book has been returned successfully."


# ----------------------------------------------------------------
# Main Application Logic
# ----------------------------------------------------------------
class LibrarySystem:
    def __init__(self):
        self.db = Database()
        self.current_user = None

        # Create a default admin if none exists
        self.ensure_admin_exists()

    def ensure_admin_exists(self):
        self.db.cursor.execute("SELECT COUNT(*) FROM users WHERE role='admin'")
        if self.db.cursor.fetchone()[0] == 0:
            print("No admin found. Creating default admin account...")
            self.db.add_user("Administrator", "admin@lib.com", "admin123", "admin")

    # --------------- User Login ---------------
    def login(self):
        clear()
        print("=== USER LOGIN ===\n")
        email = input("Email: ")
        password = input("Password: ")

        user = self.db.authenticate(email, password)
        if user:
            self.current_user = {
                "id": user[0],
                "name": user[1],
                "role": user[2]
            }
            print(f"\nWelcome, {self.current_user['name']}!")
        else:
            print("\nInvalid login.")

    # --------------- Admin Menu ---------------
    def admin_menu(self):
        while True:
            clear()
            print("==== ADMIN PANEL ====\n")
            print("1. Add User")
            print("2. Add Book")
            print("3. View Books")
            print("4. Search Books")
            print("5. Logout")
            choice = input("\nEnter choice: ")

            if choice == "1":
                self.add_user()
            elif choice == "2":
                self.add_book()
            elif choice == "3":
                self.view_books()
            elif choice == "4":
                self.search_books()
            elif choice == "5":
                break

            input("\nPress ENTER...")

    # --------------- Member Menu ---------------
    def member_menu(self):
        while True:
            clear()
            print("==== USER PANEL ====\n")
            print("1. View Books")
            print("2. Search Books")
            print("3. Borrow Book")
            print("4. Return Book")
            print("5. Logout")
            choice = input("\nEnter choice: ")

            if choice == "1":
                self.view_books()
            elif choice == "2":
                self.search_books()
            elif choice == "3":
                self.borrow_book()
            elif choice == "4":
                self.return_book()
            elif choice == "5":
                break

            input("\nPress ENTER...")

    # ----------------------------------------------------------------
    # Feature Implementations
    # ----------------------------------------------------------------
    def add_user(self):
        print("\n=== Add User ===")
        name = input("Name: ")
        email = input("Email: ")
        password = getpass("Password: ")
        role = input("Role (admin/member): ").lower()

        if role not in ("admin", "member"):
            print("Invalid role.")
            return

        self.db.add_user(name, email, password, role)
        print("User created successfully!")

    def add_book(self):
        print("\n=== Add Book ===")
        title = input("Title: ")
        author = input("Author: ")
        category = input("Category: ")
        isbn = input("ISBN: ")
        self.db.add_book(title, author, category, isbn)
        print("Book added successfully!")

    def view_books(self):
        books = self.db.get_books()
        print("\n=== BOOK LIST ===\n")
        for b in books:
            status = "Available" if b[5] else "Issued"
            print(f"{b[0]} | {b[1]} | {b[2]} | {b[3]} | {b[4]} | {status}")

    def search_books(self):
        keyword = input("\nEnter keyword: ")
        books = self.db.search_books(keyword)
        print("\n=== SEARCH RESULTS ===\n")
        for b in books:
            status = "Available" if b[5] else "Issued"
            print(f"{b[0]} | {b[1]} | {b[2]} | {b[3]} | {b[4]} | {status}")

    def borrow_book(self):
        book_id = input("\nEnter Book ID: ")
        msg = self.db.borrow_book(self.current_user["id"], book_id)
        print(msg)

    def return_book(self):
        book_id = input("\nEnter Book ID: ")
        msg = self.db.return_book(book_id)
        print(msg)


# ----------------------------------------------------------------
# Run Application
# ----------------------------------------------------------------
app = LibrarySystem()

while True:
    app.login()
    if not app.current_user:
        input("\nPress ENTER...")
        continue

    if app.current_user["role"] == "admin":
        app.admin_menu()
    else:
        app.member_menu()

