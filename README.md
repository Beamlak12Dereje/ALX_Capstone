# ALX_Capstone
Capstone Project Part 1: Planning Document
Project Title:- Simple Personal Task Manager
Project Idea:
This project is a web-based personal task manager built using Django. It allows users to register, log in, and manage their daily tasks. Each user can add new tasks, set due dates, mark them as complete/incomplete, and view only their own task list.
The goal is to apply Django fundamentals in a real project—covering models, views, forms, templates, authentication, and CRUD operations.
Main Features:
User Authentication:


User registration (sign up)
User login/logout


Task Management:


Add a task
View all tasks
Edit a task
Delete a task
Mark a task as complete or incomplete


User-Specific Data:


Each user sees only their own tasks


(Optional) Task due dates and filtering by status or date


API (Optional):
No external API required.
All data will be handled internally using Django’s ORM and models.



Project Structure (Apps & Endpoints):
Apps:
users: Handles authentication (registration, login/logout)
tasks: Handles task creation, editing, listing, deleting, and toggling status


Endpoints:
URL
Method
Function
/register/
GET/POST
Register a new user
/login/
GET/POST
Log in an existing user
/logout/
GET
Log out
/tasks/
GET
View all tasks for the logged-in user
/tasks/create/
GET/POST
Create a new task
/tasks/<id>/edit/
GET/POST
Edit an existing task
/tasks/<id>/delete/
POST
Delete a task
/tasks/<id>/toggle/
POST
Mark task as complete/incomplete

Timeline (5 Weeks):
Week
Goals
1
Initialize Django project, create apps, configure settings/templates
2
Implement user registration and login/logout
3
Create task model and implement CRUD for tasks
4
Add features: due dates, task filtering, and toggle status
5
Finalize UI, test thoroughly, debug issues, and prepare for review

Additional Planning Notes:
Authentication will use Django’s built-in User model and auth views.
Templates will be styled using Bootstrap for a clean interface.
Use login_required to secure routes.
All task views will filter tasks by request.user to isolate user data.
Keep code modular and reusable between apps.
