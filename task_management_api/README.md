# Task Management API

## Features
- Custom User model (username, bio, profile picture)
- Token authentication (DRF token)
- Register / Login / Profile endpoints
- Task CRUD endpoints (each task belongs to an authenticated user)

## Setup
1. Create and activate virtualenv
2. Install dependencies:
   pip install django djangorestframework djangorestframework-authtoken
3. Run migrations:
   python manage.py makemigrations
   python manage.py migrate
4. Create superuser (optional):
   python manage.py createsuperuser
5. Start server:
   python manage.py runserver

## Endpoints
- POST /api/auth/register/  -> register (returns token)
- POST /api/auth/login/     -> login (returns token + user)
- GET/PUT /api/auth/profile/ -> profile (auth required)
- CRUD /api/tasks/tasks/     -> tasks endpoints (auth required)


