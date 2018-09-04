from app import app, db
from flask import request
import json
from app.models import Profile



@app.route("/profile/", methods=["GET"])
def get_profile1():
    if request.method == "GET":
        response = []
        for user in Profile.query.all():
            response.append({
                'id': user.id,
                'firstname': user.firstname,
                'lastname': user.lastname,
                'email': user.email,
                'user_id': user.user_id
            })
        return json.dumps(response)


@app.route("/profile/<int:profile_id>", methods=["PUT"])
def profile1(profile_id):
    if Profile.query.filter(Profile.id == profile_id).first():
        if request.method == "PUT":
            new_username = request.form.get('firstname', None)
            if new_username:
                update_info = Profile.query.filter(Profile.id == profile_id).first()
                update_info.firstname = new_username
                db.session.commit()
                return "NEW info: \n" + str(update_info)
            else:
                return 'Doesnt work'
    return "Doesnt work"
