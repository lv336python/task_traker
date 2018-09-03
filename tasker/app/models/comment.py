import datetime

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from .. import db


class Comment(db.Model):
    __tablename__ = "comments"
    id = Column(Integer, autoincrement=True, primary_key=True)
    date = Column(DateTime, nullable=False, default=datetime.datetime.now)
    body = Column(String(255), nullable=False)
    comment_to_response = Column(Integer, ForeignKey('comments.id'), nullable=True)
    response_relationship = relationship("Comment")
    is_response = Column(Boolean, nullable=False, default=False)

    def __init__(self, date, body, comment_to_response=None):
        self.date = date
        self.body = body
        self.comment_to_response = comment_to_response
        if comment_to_response:
            self.is_response = True
        else:
            self.is_response = False

    def __repr__(self):
        if self.is_response:
            return f"Comment #{self.id}:\n\tDate:{self.date}\n\t" \
                   f"Answer to {self.comment_to_response} Body:{self.body}"
        else:
            return f"Comment #{self.id}:\n\tDate:{self.date}\n\tBody:{self.body}"

