from tasker.app import app

@app.route("/")
def hello():
    return '<h1>VOva</h1>'
