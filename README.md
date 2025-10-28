# 🗂️ Task Management API

A **Django REST Framework-based API** for managing tasks, organizing categories, notifying users, and handling user authentication.  
This project demonstrates clean architecture, modular app design, and production-ready deployment on **PythonAnywhere**.

---

## 🚀 Live Demo
🔗 **API URL:** [https://hanna3030.pythonanywhere.com](https://hanna3030.pythonanywhere.com)

---

## 📑 Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Environment Variables](#environment-variables)
- [Running the Project](#running-the-project)
- [API Endpoints](#api-endpoints)
- [Deployment](#deployment)
- [Author](#author)

---

## Overview
The **Task Management API** is designed to help users:
- Create, organize, and track tasks.
- Categorize tasks for better organization.
- Receive notifications about deadlines and updates.
- Manage user authentication and profiles.

The project follows **Django’s modular design** principles — separating logic into dedicated apps for scalability and maintainability.

---

## Features
-  **User Authentication** — Secure registration, login, and token-based authentication.
-  **Task Management** — CRUD operations for tasks with deadlines, priorities, and status updates.
-  **Category System** — Group and organize tasks under custom categories.
-  **Notifications** — Receive task-related alerts or reminders.
-  **Admin Dashboard** — Manage users, tasks, and categories through Django Admin.
-  **Deployed API** — Live and accessible through PythonAnywhere.

---

##  Project Structure
```
Task_Management_API/
│
├── manage.py
├── requirements.txt
├── README.md
├── db.sqlite3
│
├── project/                 # Main project configuration
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│
├── tasks/                   # Manages task creation, updates, and deletion
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│
├── notifications/           # Handles task alerts and notifications
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│

```

---

## 🧰 Tech Stack
- **Backend Framework:** Django 5.1 + Django REST Framework
- **Database:** SQLite3 (development)
- **Hosting:** PythonAnywhere
- **Language:** Python 3.13
- **Version Control:** Git & GitHub

---

## Installation

### 1️⃣ Clone the repository
```bash
git clone https://github.com/Hannah3012/Task_Management_API.git
cd Task_Management_API
```

### 2️ Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate    # On Linux/Mac
venv\Scripts\activate       # On Windows
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Apply migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5️⃣ Create a superuser
```bash
python manage.py createsuperuser
```

### 6️⃣ Run the development server
```bash
python manage.py runserver
```

---



## 🔗 API Endpoints


### 🔸 Tasks
| Method | Endpoint | Description |
|--------|-----------|-------------|
| GET | `/api/tasks/` | List all tasks |
| POST | `/api/tasks/` | Create new task |
| PUT | `/api/tasks/{id}/` | Update a task |
| DELETE | `/api/tasks/{id}/` | Delete a task |


### 🔸 Notifications
| Method | Endpoint | Description |
|--------|-----------|-------------|
| GET | `/api/notifications/` | View notifications |
| POST | `/api/notifications/` | Create a notification |

---

## ☁️ Deployment (PythonAnywhere)

1. Push your project to GitHub.  
2. Log in to [PythonAnywhere](https://www.pythonanywhere.com/).  
3. Clone your repo inside `/home/<username>/project/`.  
4. Set up a virtual environment and install requirements:
   ```bash
   pip install -r requirements.txt
   ```
5. Run migrations:
   ```bash
   python manage.py migrate
   ```
6. Configure WSGI file and static files.
7. Reload your web app.

---


## 👩‍💻 Author
**Hanna Tariku**  
Full-stack Developer | Passionate about secure, impactful web platforms.  

