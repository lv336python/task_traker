from sqlalchemy import Column, Integer, String, Boolean
from app import db


class Profile(Base):
    __tablename__ = 'profile'
    id = Column(Integer, primary_key=True)
    email = Column(String(120), unique=True)
    password = Column(String(64))

    def __init__(self, email=None, password=None):
        self.email = email
        self.password = password

    def __repr__(self):
        return '<Profile {}>'.format(self.id)
