# 📝 Django Todo Service (MVP)

This project is a minimal prototype of a Todo service built with Django.  
Goal: to have a fully functional backend with CRUD, authentication, filtering, and minimal UI for testing logic.

---

## 📦 Features

- Create, edit, delete tasks (`Task`)  
- Task categories (`Category`)  
- User-specific task assignment  
- Filtering tasks by category, status, and deadline  
- Mark overdue tasks  
- Minimal HTML templates (text + basic buttons)  
- Admin panel for model management  
- User authentication (register, login, logout)  
- Deployed on Railway  

---

## 🛠 Technologies

- Python 3.14  
- Django 5.2.8  
- Django REST Framework 3.16.1  
- Gunicorn 21.2.0  
- SQLite (for MVP)  
- Railway (deployment)  

---

## 🚀 Local Setup

1. Clone the repository:  
```bash
git clone git@github.com:JoKer36627/Django-ToDo.git
cd Django-ToDo

	2.	Create and activate a virtual environment:

python3 -m venv .venv
source .venv/bin/activate  # Mac/Linux
.venv\Scripts\activate     # Windows

	3.	Install dependencies:

pip install -r requirements.txt

	4.	Apply migrations:

python manage.py migrate

	5.	Run the server:

python manage.py runserver

	•	Open http://127.0.0.1:8000/tasks-page/￼ to view tasks
	•	Open http://127.0.0.1:8000/admin/￼ for the admin panel

⸻

🧩 Project Structure

ToDo_Django/
├── core/              # main app with models, serializers, views, urls
├── todoservice/       # Django project configuration (settings, urls, wsgi)
├── templates/         # minimal HTML templates
├── db.sqlite3         # MVP database
├── manage.py
├── requirements.txt
├── runtime.txt
└── Procfile           # for Railway deployment


⸻

⚙️ Deployment on Railway
	1.	Add your GitHub repository
	2.	Deploy through Railway → Deploy from GitHub
	3.	Add environment variables:
	•	ALLOWED_HOSTS=web-production-XXXX.up.railway.app
	•	CSRF_TRUSTED_ORIGINS=https://web-production-XXXX.up.railway.app
	4.	Run migrations on the server:

python manage.py migrate


⸻

🧪 MVP Testing
	•	Full user flow: register → login → create tasks → filter → mark completed → check overdue
	•	Admin panel for adding/editing categories and tasks

⸻

⚠️ Notes
	•	UI is minimal, no design
	•	For production, set DEBUG=False and secure your secrets
	•	SQLite is used for MVP; PostgreSQL is recommended for production
