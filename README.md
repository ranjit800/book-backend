### ✅ **Backend: `book-backend/README.md`**

# MyPustak Book API (Backend)

This is the Django REST Framework backend for the MyPustak Book App. It provides APIs to fetch books and submit book orders.

## Live Deployment

Backend is hosted on Render:

**URL:** [https://book-backend-hk0w.onrender.com](https://book-backend-hk0w.onrender.com)

## GitHub Repository

**Repo:** [https://github.com/ranjit800/book-backend](https://github.com/ranjit800/book-backend)

## Tech Stack

- Django 5.x
- Django REST Framework
- SQLite (default)
- Render (for deployment)

## Project Structure

```
book-backend/
├── bookapi/              # Main Django project
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── books/                # App with models and views
├── db.sqlite3
├── requirements.txt
└── README.md
```

## API Endpoints

| Method | Endpoint     | Description                |
|--------|--------------|----------------------------|
| GET    | `/books/`    | List all available books   |
| POST   | `/order/`    | Submit an order            |

## Local Setup

```bash
git clone https://github.com/ranjit800/book-backend.git
cd book-backend
python -m venv env
source env/bin/activate  # or `env\Scripts\activate` on Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Render Deployment

### Root Directory
```
book-backend
```

### Start Command
```
gunicorn bookapi.wsgi:application
```

### Environment Variables

| Key            | Value                          |
|----------------|--------------------------------|
| SECRET_KEY     | your-django-secret-key         |
| DEBUG          | False                          |
| PYTHON_VERSION | 3.11.9                         |

## CORS Setup (`settings.py`)

```python
CORS_ALLOWED_ORIGINS = [
    "http://localhost:8081",
    "https://mypustak-book-app.netlify.app",
]
```