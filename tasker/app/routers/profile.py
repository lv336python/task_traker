import json
from flask import request, session

from app.models import Profile
from app import app, db


@app.route("/profile", methods=["GET"])
def get_profile1():
    """
    Method GET if User is logged in
    :return: Json user data
    """
    user_id = session['user_id']
    print(user_id)
    profile = Profile.query.filter(Profile.user_id == user_id).first()
    if profile:
        response = []
        response.append({
                'id': profile.id,
                'firstname': profile.firstname,
                'lastname': profile.lastname,
                'email': profile.email,
                'user_id': profile.user_id
            })
        return json.dumps(response)
    else:
        return json.dumps({'status': 404,
                          'message': "profile not found"}), 404


@app.route("/profile/<int:profile_id>", methods=["PUT"])
def profile(profile_id):
    """
    Method PUT if User is ligged in
    :param profile_id:
    :return: New logged in user firstname or 40x status
    """
    user_id = session['user_id']
    if user_id == profile_id:
        profile = Profile.query.filter(Profile.id == profile_id).first()
        new_name = request.form.get('firstname', None)
        if new_name:
            profile.firstname = new_name
            db.session.commit()
            return profile.to_json(), 200
        else:
            return json.dumps({'status': 400,
                        'message': "empty value"}), 400
    return json.dumps({'status': 404,
                      'message': "profile not found"}), 404
