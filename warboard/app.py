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

@app.route("/users", methods=["POST", "GET"])
def project_methods():
    request = app.current_request
    client = boto3.client("dynamodb")
    tables = client.list_tables().get("TableNames")
    for table in tables:
        if "personTable" in table:
            person_table_name = table

    request_method = app.current_request.method
    dynamo_resource = boto3.resource("dynamodb")
    person_table = dynamo_resource.Table(person_table_name)

    if request_method == "POST":
        person_table.put_item(
            Item=request.json_body

        )
    # Retrieve existing users
    if request_method == "GET":
        return person_table.scan().get("Items")

@app.route("/users/{user}", methods=["GET", "PUT", "DELETE"])
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
    if request_method == "PUT":
        user_table.update_item(
            Key={
                "UserName" : user,
                },
            UpdateExpression='SET Country = :val1, Id = :val2',
            ExpressionAttributeValues={
                ':val1': 'US',
                ':val2': 123
            }
        )
    # Retrieve existing user
    if request_method == "GET":
        retrieved_user = user_table.get_item(
            Key={
                "UserName": user
            }
        ).get("Item")
        return retrieved_user

    if request_method == "DELETE":
        retrieved_user = user_table.delete_item(
            Key={
                "UserName": user
            }
        )

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
