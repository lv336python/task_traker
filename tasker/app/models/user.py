from app import db
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password = db.Column(db.String(128))

    @staticmethod
    def create (username, password):
        user = User()
        user.username = username
        user.password = generate_password_hash(password)
        db.session.add(user)
        db.session.commit()

    def check_password(self, pw):
        return check_password_hash(self.password, pw)

    def __repr__(self):
        return '<User {}>'.format(self.username)
    
