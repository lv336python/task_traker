from app import app, db
from flask import render_template, request
import json
from app.models.profile import Profile


@app.route('/user/<string:username>')
def user1(username):
    if Profile.query.filter(Profile.username == username):
        user = Profile.query.filter(Profile.username == username).first()
        return render_template('user.html', user=user)


@app.route("/profile/", methods=["GET"])
def get_profile1():
    if request.method == "GET":
        response = []
        for user in Profile.query.all():
            response.append({
                'id': user.id,
                'username': user.username,
                'email': user.email,
            })
        return json.dumps(response)


@app.route("/profile/<int:profile_id>", methods=["PUT"])
def profile1(profile_id):
    if Profile.query.filter(Profile.id == profile_id).first():
        if request.method == "PUT":
            new_username = request.form.get('username', 'RandomName')
            if new_username:
                update_info = Profile.query.filter(Profile.id == profile_id).first()
                update_info.username = new_username
                db.session.commit()
                return "NEW info: \n" + str(update_info)
            else:
                return 'Doesnt work'
    return "Doesnt work"
