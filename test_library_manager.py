import pytest
from library_manager import add_book, remove_book, list_books

def test_add_book():
    library = []
    assert add_book(library, "Book A") == ["Book A"]

def test_remove_book():
    library = ["Book A"]
    assert remove_book(library, "Book A") == []

def test_list_books():
    library = ["Book A"]
    assert list_books(library) == ["Book A"]

def test_search_book():
    library = ["Book A", "Book B"]
    assert search_book(library, "Book A") == ["Book A"]

