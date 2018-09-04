from app import app, db
from flask import render_template, request
import json
from app.models.registration import Registration
from app.models.user import User


@app.route('/registration', methods=['POST'])
def registration():
    if request.method == 'POST':
        data = json.loads(request.data)
        # username = request.form['username']
        # password = request.form['password']
        User.create(data['username'], data['password'])
        return data['username'] + ' are registered'
    else:
        return 'Invalid data' \


@app.route('/registration')
def registration_get():
    # return 'hello'
        return render_template('registration.html')
    
