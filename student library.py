username = "admin"
password = "12345"
def login():
    print("------- LOGIN-------")
    while True:
        u=input("enter username: ")
        p=input("enter password: ")

        if u == username and p == password:
             print("your login has been successful")
             break
        else:
            print("incorrect login.try again")
login()

books = {

    "B001": {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "available": True},
    "B002": {"title": "1984", "author": "George Orwell", "available": True},
    "B003": {"title": "To Kill a Mockingbird", "author": "Harper Lee", "available": False}
}
       
def add_book():
    book_id = input("Enter book ID: ")
    title = input("Enter title: ")
    author = input("Enter author: ")
    books[book_id] = {"title": title, "author": author, "available": True}
    print(f"Book '{title}' added successfully.")

def remove_book():
    book_id = input("Enter book ID to remove: ")
    if book_id in books:
        del books[book_id]
        print("Book removed successfully.")
    else:
        print("Book not found.")

def display_books():
    print("\n--- Library Books ---")
    for book_id, details in books.items():
        status = "Available" if details["available"] else "Issued"
        print(f"ID: {book_id}, Title: {details['title']}, Author: {details['author']}, Status: {status}")

# --- Member Database ---

members = {
    "M001": {"name": "kajal", "borrowed_books": []},
    "M002": {"name": "teenu", "borrowed_books": ["B003"]}
}

def add_member():
    member_id = input("Enter member ID: ")
    name = input("Enter member name: ")
    members[member_id] = {"name": name, "borrowed_books": []}
    print(f"Member '{name}' added successfully.")           

def remove_member():
    member_id = input("Enter member ID to remove: ")
    if member_id in members:
        del members[member_id]
        print("Member removed successfully.")
    else:
        print("Member not found.")

def display_members():
    print("\n--- Library Members ---")
    for member_id, details in members.items():
        print(f"ID: {member_id}, Name: {details['name']}, Borrowed Books: {', '.join(details['borrowed_books'])}")

# --- Borrow/Return Operations ---
def borrow_book():
    member_id = input("Enter member ID: ")
    book_id = input("Enter book ID to borrow: ")

    if member_id in members and book_id in books:
        if books[book_id]["available"]:
            books[book_id]["available"] = False
            members[member_id]["borrowed_books"].append(book_id)
            print(f"Book '{books[book_id]['title']}' borrowed by '{members[member_id]['name']}'.")
        else:
            print("Book is currently unavailable.")
    else:
        print("Invalid member ID or book ID.")

