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
