from datetime import datetime
from app import db


class Task(db.Model):
    __tablename__ = 'tasks'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer , db.ForeignKey('user.id'), nullable=False)
    name = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text, nullable=True)
    is_active = db.Column(db.Boolean)
    created_date = db.Column(db.DateTime, nullable=False, default=datetime.now())
    updated_date = db.Column(db.DateTime, nullable=False, default=datetime.now())

    def __init__(self, name, description, created_date, updated_date):
        self.name = name
        self.description = description
        self.created_date = created_date
        self.updated_date = updated_date

    def __repr__(self):
        return f"Task#{id}\tname : {self.name}\nCreated: { self.created_date }\tUpdated:{self.updated_date}"
