User Authentication and Role-Based Access System:
This project implements a simple user authentication and role-based access control (RBAC) system using Django, Django Rest Framework, 
and JWT tokens. The system supports three types of users: Admin, User, and Moderator. 
Users can register, log in, and access specific views based on their roles.

Features:
User Registration: Users can register by providing a username, email, and password.

Role-Based Access Control:
Admin users can access admin-specific views.
Regular users can access user-specific views.
Moderators can access moderator-specific views.
JWT Authentication: Uses JWT tokens (access and refresh tokens) for user authentication.
Role Management: Users are assigned roles upon registration.
