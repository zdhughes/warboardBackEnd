# Warboard backend API

https://7wpxm2y4dc.execute-api.us-east-1.amazonaws.com/dev/

API Gateway deplyed via Chalice.
Backed by DynamoDB for persistent data.

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
Returns all details for the indicated project
## PUT /projects/{project}
Updates the indicated project's attributes
## DELETE /projects/{project}
Deletes the indicated project
## GET /users/{user}
Returns all details for the indicated user
## PUT /users/{user}
Updates a specific user's attributes
## DELETE /users/{user}
Deletes the indicated user
## GET /projects/{project}/status
Returns a specific project's resourcing status
## PUT /projects/{project}/status
Updates the provided project's resourcing status, given the project's currently assigned team

User Data Model: 
Id:	87
Position:	engineer
UserName: zachary

Project Data Model: 
End: 2017-06-30
Id:	100
ProjectName: MomCorp
RequirementsMap:
  architect:	1
  engineer:	2
  pm:	1
resourced: true
Start: 2017-04-01
Team: 
  mikko
  yvonne
  clark
  sean
  zachary

# TODO
- Add Google Authentication
- Add user's availability and match against project requirements, with suggestions.
- Add skills matching between projects and users
- Import data from current resource spreadsheet
- Import data from current skills spreadsheet
