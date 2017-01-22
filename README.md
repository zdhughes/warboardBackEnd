# Warboard backend API

API Gateway backed by DynamoDB

Currently supported APIs:
## GET /projects
Returns the list of projects
## POST /projects
Creates a new project
## GET /users
Returns the list of users
## POST /users
Creates a new user
## GET /projects/{project}
Returns the details about a specific project
## PUT /projects/{project}
Updates a specific project's attributes
## DELETE /projects/{project}
Deletes a project
## GET /users/{user}
Returns the details about a specific user
## PUT /users/{user}
Updates a specific user's attributes
## DELETE /users/{user}
Deletes a user
## GET /project/{project}/status
Returns a specific project resourcing status
## PUT /project/{project}/status
Updates a specific project resourcing status automatically
