from app import db


class Registration(db.Model):
    __tablename__ = "registration"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)

    def __init__(self, username, email):
        self.username = username
        self.email = email


    def __repr__(self):
        return f'User: {self.username}'