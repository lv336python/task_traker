from flask import request, session

from app import app
from app.models.user import User


@app.route("/login", methods=['POST'])
def login():

    if request.method == 'POST':
        data = request.get_json()
        user = User.query.filter_by(username=data['username']).first()
        if user and user.check_password(pw=data['password']):
            session['logged_in'] = True
            return data['username'] + ' are logged'
        else:
            return 'Invalid data'


@app.route('/logout')
def logout():
    session.pop('username', None)
    return 'logged out'

