import json
from flask import request

from app.models import Profile, User
from app import app, db


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
    else:
        return json.dumps({'status': 404,
                          'message': "profile not found"}), 404


@app.route("/profile/<int:profile_id>", methods=["PUT"])
def profile1(profile_id):
    profile = Profile.query.filter(Profile.id == profile_id).first()
    if profile:
        if request.method == "PUT":
            new_name = request.form.get('firstname', None)
            if new_name:
                profile.firstname = new_name
                db.session.commit()
                return profile.to_json(), 200
            else:
                json.dumps({'status': 400,
                            'message': "empty value"}), 400
    return json.dumps({'status': 404,
                      'message': "profile not found"}), 404
