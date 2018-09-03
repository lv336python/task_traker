import json
from app import app
from flask import jsonify, request, session
from app.models.user import User


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        response = []
        for user in User.query.all():
            response.append({'id': user.id,
                             'username': user.username,
                             'password': user.password,
                             })
        return json.dumps(response)

    elif request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=data['username']).first()
        if user and user.check_password(password):
            session['logged_in'] = True
            return username + ' are logged'
        else:
            return 'Invalid data'


@app.route('/logout')
def logout():
    session['logged_in'] = False
    return 'Now u are logged out'
