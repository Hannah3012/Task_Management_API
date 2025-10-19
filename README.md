# 🧩 Task Manager API — Django REST Framework

A **Task Management API** built with **Django** and **Django REST Framework (DRF)** that provides full CRUD functionality for managing tasks and users. It includes authentication, ownership restrictions, filtering, and deployment readiness for production environments like Heroku and PythonAnywhere.

---

## 🚀 Features

### ✅ Core Functionalities
- **User Management (CRUD)**  
  Create, read, update, and delete users securely.
- **Task Management (CRUD)**  
  Each user can manage their own tasks with fields such as:
  - Title
  - Description
  - Due Date
  - Priority (Low, Medium, High)
  - Status (Pending, Completed)
  - Completed timestamp
- **Task Completion Control**  
  - Mark tasks as complete/incomplete via a dedicated endpoint.  
  - Completed tasks cannot be edited unless reverted to *Pending*.
- **Filtering & Sorting**  
  Filter tasks by `status`, `priority`, or `due date`.  
  Sort by `due_date` or `priority`.
- **Task Ownership**  
  Each user can only access and manage their own tasks.

---

## 🧱 Tech Stack

| Component | Technology |
|------------|-------------|
| Backend Framework | Django 5 + Django REST Framework |
| Authentication | JWT (via `djangorestframework-simplejwt`) & Session Auth |
| Filtering | django-filter |
| Database | SQLite (local) / PostgreSQL (production) |
| Deployment | Heroku / PythonAnywhere |

---

## 🔑 Authentication

You can authenticate using **JWT** or Django’s **Session Authentication**.

### Obtain Token
```bash
POST /api/token/
{
  "username": "alice",
  "password": "password123"
}
```
Response:
```json
{
  "access": "<jwt_access_token>",
  "refresh": "<jwt_refresh_token>"
}
```

### Refresh Token
```bash
POST /api/token/refresh/
{
  "refresh": "<jwt_refresh_token>"
}
```

## 🧠 API Endpoints

| Endpoint | Method | Description |
|-----------|---------|--------------|
| `/api/users/` | `POST` | Register a new user |
| `/api/token/` | `POST` | Obtain JWT token |
| `/api/tasks/` | `GET` | List all tasks for the authenticated user |
| `/api/tasks/` | `POST` | Create a new task |
| `/api/tasks/{id}/` | `GET` | Retrieve a specific task |
| `/api/tasks/{id}/` | `PUT/PATCH` | Update a task (if not completed) |
| `/api/tasks/{id}/` | `DELETE` | Delete a task |
| `/api/tasks/{id}/mark/` | `POST` | Mark a task as complete/incomplete |

### Filtering & Sorting
```bash
GET /api/tasks/?status=pending&priority=high&ordering=due_date
```

---

## 🧪 Testing

Run tests using Django’s built-in test framework:
```bash
python manage.py test
```

Basic tests verify:
- Task creation with valid data
- Ownership restrictions
- Completed task immutability
- Filtering and ordering functionality

---

## ☁️ Deployment

### Heroku Deployment Steps
1. Create a Heroku app:  
   ```bash
   heroku create taskmanager-api
   ```
2. Add PostgreSQL add-on:  
   ```bash
   heroku addons:create heroku-postgresql:hobby-dev
   ```
3. Push code to Heroku:  
   ```bash
   git push heroku main
   ```
4. Run migrations:  
   ```bash
   heroku run python manage.py migrate
   ```

For **PythonAnywhere**, upload your repo, configure the WSGI app, and set environment variables accordingly.

---

## 🧩 Folder Structure
```
project_root/
│
├── taskmanager_project/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── tasks/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── permissions.py
│   ├── urls.py
│   └── tests.py
│
├── requirements.txt
├── Procfile
└── manage.py
```

---

## 🧱 Validations & Business Rules
- **Due Date Validation:** must be in the future.
- **Priority Restriction:** only `low`, `medium`, `high` allowed.
- **Status Validation:** `pending` or `completed` only.
- **Edit Restriction:** completed tasks cannot be edited unless reverted.
- **Ownership Rule:** each user only sees their own tasks.

