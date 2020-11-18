import uuid
from datetime import datetime, timedelta, timezone, date
from pydantic import BaseModel


class Book(BaseModel):
    book_id: uuid.UUID = uuid.uuid4()
    borrow_date: date = datetime.now(timezone.utc)
    return_date: date = datetime.now(timezone.utc) + timedelta(hours=1)

    def __repr__(self):
        return str(self.book_id)

    def __str__(self):
        return str(self.book_id)

    @property
    def days(self):
        "Get the days elapsed between borrow and return dates"
        elapsed = self.return_date - self.borrow_date
        return elapsed.days

    @property
    def charges1(self):
        if self.days <= 0:
            return 1
        return self.days

    def to_dict(self):
        return {
            "book_id": str(self.book_id),
            "borrow_date": self.borrow_date.isoformat(),
            "return_date": self.return_date.isoformat(),
            "charges": self.charges1,
            "days": self.days,
        }
