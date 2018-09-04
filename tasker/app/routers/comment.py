import json
import datetime
from flask import request, session, abort

from app.models import Comment, User
from .. import app, db


@app.route("/comments/", methods=["GET", "POST"])
def comments():
    """
    Reacts to GET and POST methods
    If method GET, then function returns json of all comment objects.
    If method POST, then parses form for 'body' and 'comment_to_response'
    objects and creates a new comment
    :return: String with verbal status of response
    """
    session['user_id'] = 1
    if request.method == "GET":
        response = []
        for comment in Comment.query.all():
            response.append({'id': comment.id,
                             'date': comment.date.strftime("%Y:%M:%D  %H:%M:%S"),
                             'body': comment.body,
                             'comment_to_response': comment.comment_to_response,
                             'is_response': comment.is_response,
                             'user_id': comment.user_id})
        return json.dumps(response), 200

    else:
        body = request.form["body"]
        comment_to_response = request.form.get("comment_to_response", None)
        user_id = session.get('user_id', None)
        if user_id is None:
            abort(401)
        if comment_to_response and not Comment.query.filter(Comment.id == comment_to_response).first():
            return
        else:

            new_comment = Comment(datetime.datetime.now(),
                                  body=body,
                                  comment_to_response=comment_to_response,
                                  user_id=user_id)
            db.session.add(new_comment)
            db.session.commit()
            return new_comment.to_json(), 201



@app.route("/comments/<int:comment_id>", methods=["PUT", "DELETE"])
def comment(comment_id):
    """
    Updates or deletes comment depending on the method used.
    :param comment_id: integer which represents comment id in DB
    :return: String with verbal status of response
    """
    comment_to_update = Comment.query.filter(Comment.id == comment_id).first()
    if comment_to_update:
        if session['user_id'] == comment_to_update.user_id:
            if request.method == "PUT":
                body = request.form.get("body", None)
                if body:
                    comment_to_update.body = body
                    db.commit()
                    return "UPDATED\n" + str(comment_to_update)
                else:
                    return "FAILED"

            else:
                db.delete(Comment.query.filter(Comment.id == comment_id).first())
                db.commit()
                return "DELETED"
    else:
        return "FAILED"
