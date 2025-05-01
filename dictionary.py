library = [
    {
        "title": "The Road Ahead",
        "author": "Bill Gates",
        "isLoaned": True
    },
    {
        "title": "Steve Jobs",
        "author": "Walter Isaacson",
        "isLoaned": True
    },
    {
        "title": "Mockingjay: The Final Book of The Hunger Games",
        "author": "Suzanne Collins",
        "isLoaned": False
    }
]


def loan_status(lib):
    for book in lib:
        book_info = f"{book['title']} by {book['author']}"

        if book["isLoaned"]:
            print(f"Out on loan: {book_info}")
        else:
            print(f"On the shelf: {book_info}")


def get_books_by_author(library, author_name):
    books_by_author = []

    for book in library:
        if book["author"] == author_name:
            book_status = "Out on loan" if book["isLoaned"] else "On the shelf"
            books_by_author.append(f"{book['title']} - {book_status}")

    return books_by_author


def search_by_book_name(library, search_term):
    book_by_name = []
    for book in library:
        if book["title"] == search_term:
            book_by_name.append(book)
            break

    return book_by_name

def display_loan_totals():
    loan_count = 0
    not_on_loan = 0
    
    for book in library:
        if book["isLoaned"]:
            loan_count += 1  
        else:
            not_on_loan += 1

    print(f"Total books on loan: {loan_count}")
    print(f"Total books not on loan: {not_on_loan}")



def alter_book_status(book_title, new_status):
    for book in library:
        if book["title"] == book_title:
            book["isLoaned"] = not book["isLoaned"]
            break


def add_new_book(library, title, author, is_loaned):
    library.append({"title": title, "author": author, "isLoaned": is_loaned})
    return library


def remove_book(library, book_title):
    for book in library:
        if book["title"] == book_title:
            library.remove(book)
            break
    return library




# Example usage
author_name = "Suzanne Collins"
books_status = get_books_by_author(library, author_name)

print(f"Books by {author_name}:")
print(books_status)

loan_status(library)