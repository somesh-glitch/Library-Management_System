import os

# Book class with short variable names
class B:
    def __init__(self, bid, t, a, av=True):
        self.bid = bid      # book id
        self.t = t          # title
        self.a = a          # author
        self.av = av        # availability

    # Convert object to line for file
    def to_line(self):
        return f"{self.bid}|{self.t}|{self.a}|{self.av}\n"

# Library class
class L:
    def __init__(self, fn="library.txt"):
        self.fn = fn        # file name
        self.bs = []        # book list
        self.load()

    # Load books from file
    def load(self):
        if not os.path.exists(self.fn):
            return
        with open(self.fn, "r") as f:
            for ln in f:
                d = ln.strip().split("|")
                if len(d) == 4:
                    bid, t, a, av = d
                    self.bs.append(B(bid, t, a, av == "True"))

    # Save all books to file
    def save(self):
        with open(self.fn, "w") as f:
            for b in self.bs:
                f.write(b.to_line())

    # Add new book
    def add_b(self):
        bid = input("Book ID: ")
        t = input("Title: ")
        a = input("Author: ")
        self.bs.append(B(bid, t, a))
        self.save()
        print("Book added!\n")

    # View all books
    def view_b(self):
        if not self.bs:
            print("No books.\n")
            return
        for b in self.bs:
            s = "Available" if b.av else "Issued"
            print(b.bid, "|", b.t, "|", b.a, "|", s)
        print()

    # Search book by title
    def sea_b(self):
        k = input("Enter title: ").lower()
        f = False
        for b in self.bs:
            if k in b.t.lower():
                f = True
                s = "Available" if b.av else "Issued"
                print(b.bid, "|", b.t, "|", b.a, "|", s)
        if not f:
            print("Not found.\n")
        print()

    # Borrow book
    def bor_b(self):
        bid = input("Book ID to borrow: ")
        for b in self.bs:
            if b.bid == bid:
                if b.av:
                    b.av = False
                    self.save()
                    print("Book issued!\n")
                else:
                    print("Already issued.\n")
                return
        print("Book not found.\n")

    # Return book
    def ret_b(self):
        bid = input("Book ID to return: ")
        for b in self.bs:
            if b.bid == bid:
                if not b.av:
                    b.av = True
                    self.save()
                    print("Book returned!\n")
                else:
                    print("Not issued.\n")
                return
        print("Book not found.\n")


# ---------------- Main Program ----------------
lib = L()

while True:
    print("1.Add Book  2.View  3.Search  4.Borrow  5.Return  6.Exit")
    ch = input("Choice: ")

    if ch == "1": lib.add_b()
    elif ch == "2": lib.view_b()
    elif ch == "3": lib.sea_b()
    elif ch == "4": lib.bor_b()
    elif ch == "5": lib.ret_b()
    elif ch == "6":
        print("Bye!")
        break
    else:
        print("Invalid.\n")
