from chalice import Chalice
from chalice import NotFoundError
import boto3

app = Chalice(app_name='warboard')
app.debug = True

PROJECTS={'fitch':'cool project'}
USERS={'mikko':'cool engineer'}

@app.route('/')
def index():
    return {'hello': 'world'}

@app.route("/users/{user}", methods=["POST", "GET", "PUT"])
def user_methods(user):
    client = boto3.client("dynamodb")
    tables = client.list_tables().get("TableNames")
    for table in tables:
        if "personTable" in table:
            user_table_name = table

    request_method = app.current_request.method
    dynamo_resource = boto3.resource("dynamodb")
    user_table = dynamo_resource.Table(user_table_name)
    # Create a new user or update an existing one
    if request_method == "POST" or request_method == "PUT":
        user_table.put_item(user)
    # Retrieve existing user
    if request_method == "GET":
        returned_user = user_table.get_item(
            Key={
                "UserName": user
            }
        )
        return returned_user.get("Item")

@app.route("/projects", methods=["POST", "GET"])
def project_methods():
    request = app.current_request
    client = boto3.client("dynamodb")
    tables = client.list_tables().get("TableNames")
    for table in tables:
        if "projectTable" in table:
            project_table_name = table

    request_method = app.current_request.method
    dynamo_resource = boto3.resource("dynamodb")
    project_table = dynamo_resource.Table(project_table_name)

    if request_method == "POST":
        print "Making it into post method"
        project_table.put_item(
            Item=request.json_body

        )
    # Retrieve existing project
    if request_method == "GET":
        return project_table.scan().get("Items")

@app.route("/projects/{project}", methods=["PUT", "GET", "DELETE"])
def put_project(project):
    client = boto3.client("dynamodb")
    tables = client.list_tables().get("TableNames")
    for table in tables:
        if "projectTable" in table:
            project_table_name = table

    request_method = app.current_request.method
    dynamo_resource = boto3.resource("dynamodb")
    project_table = dynamo_resource.Table(project_table_name)
    # Create a new user or update an existing one
    if request_method == "PUT":
        project_table.update_item(
            Key={
                "ProjectName" : project,
                },
            UpdateExpression='SET Country = :val1, Id = :val2',
            ExpressionAttributeValues={
                ':val1': 'US',
                ':val2': 123
            }
        )
    if request_method == "GET":
        retrieved_project = project_table.get_item(
            Key={
                "ProjectName": project
            }
        ).get("Item")
        return retrieved_project
    if request_method == "DELETE":
        retrieved_project = project_table.delete_item(
            Key={
                "ProjectName": project
            }
        )

# The view function above will return {"hello": "world"}
# whenever you make an HTTP GET request to '/'.
#
# Here are a few more examples:
#
# @app.route('/hello/{name}')
# def hello_name(name):
#    # '/hello/james' -> {"hello": "james"}
#    return {'hello': name}



# @app.route('/users', methods=['GET'])
# def create_user():
#     # This is the JSON body the user sent in their POST request.
#     #user_as_json = app.json_body
#     # Suppose we had some 'db' object that we used to
#     # read/write from our database.
#     # user_id = db.create_user(user_as_json)
#     return USERS

# @app.route('/users/{user}', methods=['GET','PUT','DELETE'])
# def myuser(user):
#     request = app.current_request
#     if request.method == 'PUT':
#         USERS[user] = request.json_body
#     elif request.method == 'GET':
#         try:
#             return {user: USERS[user]}
#         except KeyError:
#             raise NotFoundError(user)
#     elif request.method == 'DELETE':
#         try:
#             del USERS[user]
#         except KeyError:
#             raise NotFoundError(user)

# @app.route('/projects', methods=['GET'])
# def create_project():
#     # This is the JSON body the user sent in their POST request.
#     #project_as_json = app.json_body
#     # Suppose we had some 'db' object that we used to
#     # read/write from our database.
#     # user_id = db.create_user(user_as_json)
#     return PROJECTS

# @app.route('/projects/{project}', methods=['GET','PUT','DELETE'])
# def myproject(project):
#     request = app.current_request
#     if request.method == 'PUT':
# 	PROJECTS[project] = request.json_body
#     elif request.method == 'GET':
#         try:
#             return {project: PROJECTS[project]}
#         except KeyError:
#             raise NotFoundError(project)
#     elif request.method == 'DELETE':
#         try:
#             del PROJECTS[project]
#         except KeyError:
#             raise NotFoundError(project)
