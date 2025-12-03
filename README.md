# 📚 Library Management System (Python – FOCP Project)

This is a simple **Library Management System** built using Python for the **Fundamentals of Computing & Programming (FOCP)** course.  
The project runs in the terminal and uses a text file (`lib.txt`) to store book records.

---

## 🚀 Features

### ✔ Add Books  
Add new books with **Book ID**, **Title**, and **Author**.

### ✔ View All Books  
Displays all stored books along with their **availability status**.

### ✔ Search Books  
Search for books by **title** (case-insensitive).

### ✔ Borrow Books  
Issue a book by its **Book ID**.  
Books cannot be borrowed if already issued.

### ✔ Return Books  
Return an issued book and update its availability.

### ✔ Persistent Storage  
All book data is saved in **`lib.txt`** using a simple `|` separated format.

---

## 🗂 File Structure

```
project/
│
├── main.py        # Your source code
├── lib.txt        # Auto-generated database file
└── README.md      # Project documentation
```

`lib.txt` will be created automatically when you add a book.

---

## 🧩 How It Works

### Book Class (`B`)
Represents each book with:
- `bid` – Book ID  
- `t` – Title  
- `a` – Author  
- `av` – Availability (True = Available)

### Library Class (`L`)
Handles:
- Loading/saving data  
- Adding, viewing, searching  
- Borrowing & returning  
- Managing file operations  

---

## ▶️ Running the Program

1. Make sure Python 3 is installed.
2. Run:

```bash
python main.py
```

3. Choose options from the menu:

```
1. Add Book  
2. View  
3. Search  
4. Borrow  
5. Return  
6. Exit
```

---

## 📄 Sample `lib.txt` Format

```
101|Python Basics|Guido Van Rossum|True
102|C Programming|Dennis Ritchie|False
```

---

## 🛠️ Technologies Used

- **Python 3**
- **File handling**
- **Object-Oriented Programming (OOP)**

---

## 🎓 Purpose of the Project

This project was created as part of the **FOCP (Fundamentals of Computing & Programming)** course to demonstrate:

- Basic Python programming  
- OOP concepts  
- File I/O  
- Simple data management  

---

## 🤝 Contribution

Feel free to fork the repo and improve the project!

---

## ⭐ If you like this project  
Give it a ⭐ on GitHub!
