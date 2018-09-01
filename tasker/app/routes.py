from app import app
from .models.task import TaskModel
from flask import request, template_rendered
import json
import datetime


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/tasks", methods=['GET', 'POST'])
def get_tasks():
    if request.method == 'GET':
        response = []
        tasks = TaskModel.query.all()
        for task in tasks:
            response.append(
                {'id': task.id,
                 'name': task.name,
                 'description': task.description,
                 'created_date': task.created_date,
                 'is_active': task.is_active,
                 'updated_date': task.updated_date}
            )
            return json.dumps(response)
    elif request.method == 'POST':
        name = request.form['name']
        description = request.form['description']

        new_task = TaskModel(created_date=datetime.datetime.now(), updated_date=datetime.datetime.now(), name=name,
                             description=description)
        # db.add(new_task)
        # db.commit
        return "Added new task!" + str(new_task)
