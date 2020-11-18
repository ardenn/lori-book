# This module servers as the data repository for this project.
# A DB backend would be more appropriate in production.
import uuid
from datetime import date
from pydantic import BaseModel

BOOK_TYPES = {
    "REGULAR": {"charge": 1.5, "min_days": 2, "min_charge": 2},
    "FICTION": {"charge": 3},
    "NOVEL": {"charge": 1.5, "min_days": 3, "min_charge": 4.5},
}


class Book(BaseModel):
    borrow_date: date = date.today()
    return_date: date = date.today()
    book_type: str = "REGULAR"

    def __repr__(self):
        return str(self.book_id)

    def __str__(self):
        return str(self.book_id)

    @property
    def book_id(self):
        return uuid.uuid4()

    @property
    def days(self):
        "Get the days elapsed between borrow and return dates"
        elapsed = self.return_date - self.borrow_date
        return elapsed.days

    @property
    def charges1(self):
        return self.days

    @property
    def charges2(self):
        return BOOK_TYPES[self.book_type]["charge"] * self.days

    @property
    def charges3(self):
        min_days = BOOK_TYPES[self.book_type].get("min_days", 0)
        min_charge = BOOK_TYPES[self.book_type].get("min_charge", 0)
        days = self.days
        if days <= min_days:
            return min_charge
        return min_charge + (
            BOOK_TYPES[self.book_type]["charge"] * (days - min_days)
        )

    def to_dict(self):
        return {
            "book_id": str(self.book_id),
            "book_type": self.book_type,
            "borrow_date": self.borrow_date.isoformat(),
            "return_date": self.return_date.isoformat(),
            "charges": self.charges3,
            "days": self.days,
        }
