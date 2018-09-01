from datetime import datetime
import json

from app import app
from flask import request

from .models import db_session
from .models import Comment

@app.route("/")
def hello():
    return "Hello World!"


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
            response.append({'id': comment.id,
                             'date': comment.date.strftime("%Y:%M:%D  %H:%M:%S"),
                             'body': comment.body,
                             'comment_to_response': comment.comment_to_response,
                             'is_response': comment.is_response})
        return json.dumps(response)

    else:
        body = request.form["body"]
        comment_to_response = request.form.get("comment_to_response", None)

        if comment_to_response and not Comment.query.filter(Comment.id == comment_to_response).first():
            return "FAILED"
        else:
            new_comment = Comment(datetime.now(), body=body, comment_to_response=comment_to_response)
            db_session.add(new_comment)
            db_session.commit()
            return "ADDED\n" + str(new_comment)



@app.route("/comments/<int:comment_id>", methods=["PUT", "DELETE"])
def comment(comment_id):
    """
    Updates or deletes comment depending on the method used.
    :param comment_id: integer which represents comment id in DB
    :return: String with verbal status of response
    """
    if Comment.query.filter(Comment.id == comment_id).first():
        if request.method == "PUT":
            body = request.form.get("body", None)
            if body:
                comment_to_update = Comment.query.filter(Comment.id == comment_id).first()
                comment_to_update.body = body
                db_session.commit()
                return "UPDATED\n" + str(comment_to_update)
            else:
                return "FAILED"
        else:
            db_session.delete(Comment.query.filter(Comment.id == comment_id).first())
            db_session.commit()
            return "DELETED"
    else:
        return "FAILED"
