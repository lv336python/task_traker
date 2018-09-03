import datetime

from .. import db


class Comment(db.Model):
    __tablename__ = "comments"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    date = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now)
    body = db.Column(db.String(255), nullable=False)
    comment_to_response = db.Column(db.Integer, db.ForeignKey('comments.id'), nullable=True)
    response_relationship = db.relationship("Comment")
    is_response = db.Column(db.Boolean, nullable=False, default=False)

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
