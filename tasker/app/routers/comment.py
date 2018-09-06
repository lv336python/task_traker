import json
import datetime
from flask import request, session

from app.models import Comment, User, Task
from app import app, db


@app.route("/comments/", methods=["GET", "POST"])
def comments():
    """
    Reacts to GET and POST methods
    If method GET, then function returns json of all comment objects.
    If method POST, then parses form for 'body' and 'comment_to_response'
    objects and creates a new comment
    :return: String with verbal status of response
    """
    if request.method == "GET":
        response = []
        for comment in Comment.query.all():
            response.append(comment.to_dict())
        return json.dumps(response), 200

    else:
        body = request.form["body"]
        task_id = request.form["task_id"]
        comment_to_response = request.form.get("comment_to_response", None)

        user_id = session.get('user_id', None)
        if user_id is None:
            json.dumps({'status': 401,
                        'message': "not authorized"}), 401
        if not Task.query.filter(Task.id == task_id).first():
            return json.dumps({'status': 404,
                               'message': "task not found"}), 404
        if comment_to_response and not Comment.query.filter(Comment.id == comment_to_response).first():
            return json.dumps({'status': 404,
                               'message': "comment not found"}), 404
        else:
            new_comment = Comment(datetime.datetime.now(),
                                  body=body,
                                  comment_to_response=comment_to_response,
                                  user_id=user_id,
                                  task_id=task_id)
            db.session.add(new_comment)
            db.session.commit()
            return json.dumps(new_comment.to_dict()), 201


@app.route("/comments/<int:comment_id>", methods=["PUT", "DELETE"])
def comment(comment_id):
    """
    Updates or deletes comment depending on the method used.
    :param comment_id: integer which represents comment id in DB
    :return: String with verbal status of response
    """
    comment = Comment.query.filter(Comment.id == comment_id).first()
    if comment:
        if session['user_id'] == comment.user_id:

            if request.method == "PUT":
                body = request.form.get("body", None)
                if body:
                    comment.body = body
                    db.session.commit()
                    return json.dumps(comment.to_dict()), 200
                else:
                    json.dumps({'status': 400,
                                'message': "empty value"}), 400

            else:
                db.session.delete(Comment.query.filter(Comment.id == comment_id).first())
                db.session.commit()
                return json.dumps(comment.to_dict()), 200
        else:
            json.dumps({'status': 401,
                        'message': "not authorized"}), 401
    else:
        return json.dumps({'status': 404,
                           'message': "comment not found"}), 404
