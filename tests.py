from data import Book
from datetime import datetime, timezone, timedelta


def test_charges1_1_days():
    book = Book()
    assert book.charges1 == 1


def test_charges1_0_days():
    book = Book(return_date=datetime.now(timezone.utc) + timedelta(hours=1))
    assert book.charges1 == 1
