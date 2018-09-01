import datetime

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from . import Base


class Comment(Base):
    __tablename__ = "comments"
    id = Column(Integer, autoincrement=True, primary_key=True)
    date = Column(DateTime, nullable=False, default=datetime.datetime.now)
    body = Column(String(255), nullable=False)
    comment_to_response = Column(Integer, ForeignKey('comments.id'), nullable=True)

    def __init__(self, date, body, comment_to_response=None):
        self.date = date
        self.body = body
        self.comment_to_response = comment_to_response

    def __repr__(self):
        if self.comment_to_response:
            return f"Comment #{self.id}:\n\tDate:{self.date}\n\t" \
                   f"Answer to {self.comment_to_response} Body:{self.body}"
        else:
            return f"Comment #{self.id}:\n\tDate:{self.date}\n\tBody:{self.body}"

