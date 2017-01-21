from chalice import Chalice
from chalice import NotFoundError

app = Chalice(app_name='warboard')
app.debug = True

PROJECTS={'fitch':'cool project'}
USERS={'mikko':'cool engineer'}

@app.route('/')
def index():
    return {'hello': 'world'}

# The view function above will return {"hello": "world"}
# whenever you make an HTTP GET request to '/'.
#
# Here are a few more examples:
#
# @app.route('/hello/{name}')
# def hello_name(name):
#    # '/hello/james' -> {"hello": "james"}
#    return {'hello': name}

@app.route('/users', methods=['GET'])
def create_user():
    # This is the JSON body the user sent in their POST request.
    #user_as_json = app.json_body
    # Suppose we had some 'db' object that we used to
    # read/write from our database.
    # user_id = db.create_user(user_as_json)
    return USERS

@app.route('/users/{user}', methods=['GET','PUT','DELETE'])
def myuser(user):
    request = app.current_request
    if request.method == 'PUT':
        USERS[user] = request.json_body
    elif request.method == 'GET':
        try:
            return {user: USERS[user]}
        except KeyError:
            raise NotFoundError(user)
    elif request.method == 'DELETE':
        try:
            del USERS[user]
        except KeyError:
            raise NotFoundError(user)

@app.route('/projects', methods=['GET'])
def create_project():
    # This is the JSON body the user sent in their POST request.
    #project_as_json = app.json_body
    # Suppose we had some 'db' object that we used to
    # read/write from our database.
    # user_id = db.create_user(user_as_json)
    return PROJECTS

@app.route('/projects/{project}', methods=['GET','PUT','DELETE'])
def myproject(project):
    request = app.current_request
    if request.method == 'PUT':
	PROJECTS[project] = request.json_body
    elif request.method == 'GET':
        try:
            return {project: PROJECTS[project]}
        except KeyError:
            raise NotFoundError(project)
    elif request.method == 'DELETE':
        try:
            del PROJECTS[project]
        except KeyError:
            raise NotFoundError(project)
