from app import db


class Profile(db.Model):
    __tablename__ = "profile"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    firstname = db.Column(db.String(255), nullable=False)
    lastname = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


    def __init__(self, firstname, lastname ,email, user_id):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.user_id = user_id

    def to_json(self):
        return str({
            'firstname': self.firstname,
            'lastname': self.lastname,
            'email': self.email,
            'user_id': self.user_id,
        })


    def __repr__(self):
        return f'Profile: {self.firstname} {self.lastname}'
