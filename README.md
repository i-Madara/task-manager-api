Task Manager API

A simple Task Management REST API built with Django REST Framework (DRF) that allows users to register, log in, and manage their tasks (CRUD) securely using token-based authentication.


Features
-User registration and login (via /api/auth/register/ and /api-token-auth/)
- Token authentication (each user gets a token after login)
- CRUD operations on tasks:
- Create new tasks
- View all user tasks
- Update existing tasks
- Delete completed or unwanted tasks
- Filtering (completed / pending tasks)
- Secure endpoints (users can only manage their own tasks)
- JSON-based API, easily testable with Postman

Tech Stack
- ython 3
- Django 5
- Django REST Framework
- SQLite3 (default database)
- Postman / VS Code Postman Extension for testing

Clone the Repository
git clone https://github.com/i-Madara/task-manager-api.git

Create and Activate Virtual Environment
python3 -m venv .venv
source .venv/bin/activate

Install Dependencies
pip install -r requirements.txt

Apply Migrations
python manage.py makemigrations
python manage.py migrate

Run the Server
python manage.py runserver

Server will start at:
http://127.0.0.1:8000/



Testing in Postman

*******************************************************
User Authentication
Register a New User

POST /api/auth/register/
Body (JSON):

{
  "username": "omar2",
  "email": "omar2@example.com",
  "password": "strongpass123",
  "password2": "strongpass123"
}


*******************************************************
Login (Token Authentication)

POST /api-token-auth/
Body (JSON):

{
  "username": "omar2",
  "password": "strongpass123"
}

*******************************************************
Task Endpoints
Create a Task

POST /api/tasks/
Headers:

Authorization: Token 
Content-Type: application/json


Body:

{
  "title": "Finish report",
  "description": "Write summary and attach charts",
  "deadline": "2025-10-30T18:00:00Z",
  "completed": false
}

*******************************************************
List All Tasks

GET /api/tasks/
Header:

Authorization: Token 



*******************************************************
Update a Task

PATCH /api/tasks/<id>/
Header:

Authorization: Token 


Body:

{
  "completed": true
}


*******************************************************
Delete a Task

DELETE /api/tasks/<id>/
Header:

Authorization: Token 



*******************************************************
Endpoints (Not finished)

Logout endpoint:
POST /api/auth/logout/
Header:

Authorization: Token 