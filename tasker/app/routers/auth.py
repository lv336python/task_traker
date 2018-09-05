from flask import request, session

from app import app
from app.models.user import User


@app.route("/login", methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()
    if user and user.check_password(pw=data['password']):
        session['user_id'] = user.id
        return data['username'] + ' is logged'
    else:
        return 'Invalid data'


@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return 'logged out'

