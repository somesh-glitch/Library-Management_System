📚 Library Management System (Python + SQLite)

A fully functional Library Management System built using Python and SQLite with secure login, book management, and user-based borrow tracking.
This project is designed for academic use, small libraries, and anyone learning database-backed application development.

🚀 Features
🔐 User Authentication

User registration

Secure login system

Passwords stored using hashing

Different users can have independent borrow history

📖 Book Management

Add new books

View all books

Search books by title

Track availability (Available / Issued)

📘 Borrow & Return System

Users can borrow available books

Prevents issuing already-borrowed books

Return previously borrowed books

Automatic status updates

Shows messages such as:

Book issued: <Book Title>
Book returned: <Book Title>

🧾 Borrow History Tracking

Each borrow action is logged with:

User ID

Book ID

Borrow date/time

Return date/time

This allows complete tracking of every user’s activity.

🗄 SQLite Database Integration

SQLite ensures:

Persistent storage

Zero installation required

Simple, portable .db file

Works anywhere Python runs

🛠 Technologies Used
Component	Technology
Programming Language	Python 3
Database	SQLite3
Authentication	Password hashing (SHA256)
Coding Style	Object-Oriented Programming
📂 Project Structure
📦 Library-Management-System
├── library.py           # Main program
├── database.db          # SQLite database (auto-created)
├── README.md            # Documentation
└── requirements.txt      # (Optional) dependency list

▶️ How to Run
1. Clone the repository
git clone https://github.com/<your-username>/Library-Management-System.git
cd Library-Management-System

2. Install dependencies (if used)
pip install -r requirements.txt

3. Run the program
python library.py


The SQLite database (library.db) will be created automatically on first run.

👥 User Flow
🔹 Registration

User creates an account with:

Username

Password

Password is securely hashed before storing.

🔹 Login

User must log in to perform any actions:

Borrow book

Return book

Search

View books

🔹 Borrowing a Book

System checks if the book is available

Assigns book to the logged-in user

Updates borrow_history table

🔹 Returning a Book

Marks book as available

Updates return timestamp

Provides confirmation message

🧪 Future Enhancements (Optional)

Admin user role

Email notifications

GUI using Tkinter / PyQt

REST API version

Export reports (PDF/Excel)

Fine calculation for late returns

🤝 Contributions

Pull requests are welcome!
Feel free to open an issue for bug reports or feature suggestions.

📜 License

This project is released under the MIT License, allowing personal and commercial use.

⭐ Support

If you found this useful, consider giving the repository a star⭐ on GitHub.
