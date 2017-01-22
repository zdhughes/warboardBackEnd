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
        expression_list = []
        values = {}
        n=0
        for key in app.current_request.json_body.keys():
            n+=1
            expression_list.append(key+ ' = :val'+str(n))
            values[':val'+str(n)] = app.current_request.json_body[key]

        update_expression = 'SET '+ (", ".join(expression_list))
        user_table.update_item(
            Key={
                "UserName" : user,
                },
            UpdateExpression=update_expression,
            ExpressionAttributeValues=values
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
        expression_list = []
        values = {}
        n=0
        for key in app.current_request.json_body.keys():
            n+=1
            expression_list.append(key+ ' = :val'+str(n))
            values[':val'+str(n)] = app.current_request.json_body[key]

        update_expression = 'SET '+ (", ".join(expression_list))
        project_table.update_item(
            Key={
                "ProjectName" : project,
                },
            UpdateExpression=update_expression,
            ExpressionAttributeValues=values
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
