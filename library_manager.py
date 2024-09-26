def add_book(library, book):
    library.append(book)
    return library

def remove_book(library, book):
    library.remove(book)
    return library

def list_books(library):
    return library

def search_book(library, title):
    return [book for book in library if title in book]

