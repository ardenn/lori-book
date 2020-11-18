from data import Book
from datetime import date, timedelta


def test_charges1_1_days():
    book = Book(return_date=date.today() + timedelta(days=1))
    assert book.charges1 == 1


def test_charges1_0_days():
    book = Book()
    assert book.charges1 == 0


def test_charges2_1_days():
    book = Book(return_date=date.today() + timedelta(days=1))
    assert book.charges2 == 1.5


def test_charges2_0_days():
    book = Book()
    assert book.charges2 == 0


def test_charges3_regular_less_than_min_days():
    book = Book()
    assert book.charges3 == 2


def test_charges3_regular_equal_to_min_days():
    book = Book(return_date=date.today() + timedelta(days=2))
    assert book.charges3 == 2


def test_charges3_novel_less_than_min_days():
    book = Book()
    book.book_type = "NOVEL"
    assert book.charges3 == 4.5


def test_charges3_novel_greater_than_min_days():
    book = Book(return_date=date.today() + timedelta(days=4))
    book.book_type = "NOVEL"
    assert book.charges3 == 6


def test_charges3_fiction_1_days():
    book = Book(return_date=date.today() + timedelta(days=1))
    book.book_type = "FICTION"
    assert book.charges3 == 3
