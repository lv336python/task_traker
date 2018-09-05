from app import app, db
from app.models.task import Task
from flask import request, render_template
import json
import datetime


def myconverter(date):
    if isinstance(date, datetime.datetime):
        return date.__str__()


@app.route("/tasks", methods=['GET', 'POST'])
def get_tasks():
    if request.method == 'GET':
        response = []
        tasks = Task.query.all()
        if tasks:

            for task in tasks:
                response.append(
                    {'id': task.id,
                     'user_id': task.user_id,
                     'name': task.name,
                     'description': task.description,
                     'created_date': task.created_date,
                     'is_active': task.is_active,
                     'updated_date': task.updated_date}
                )
            return json.dumps(response, default=myconverter)
        else:
            return json.dumps({'status': 404,
                               'message': 'no users'})
    elif request.method == 'POST':
        name = request.form['name']
        description = request.form['description']

        new_task = Task(created_date=datetime.datetime.now(), updated_date=datetime.datetime.now(), name=name,
                        description=description)
        db.session.add(new_task)
        db.session.commit()

        return "Added new task!" + str(new_task)


@app.route('/tasks/<id>')
def get_task(id):
    response = []
    task = Task.query.filter_by(id=id).first_or_404()
    response.append({
        'id': task.id,
        'user_id': task.user_id,
        'name': task.name,
        'description': task.description,
        'created_date': task.created_date,
        'is_active': task.is_active,
        'updated_date': task.updated_date
    })
    return json.dumps(response, default=myconverter)
