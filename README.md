# EscTrix — Futuristic Startup Website (Django Edition)

A high-performance, dark-futuristic website for **EscTrix**, offering software development, web development, UI/UX design, and animation services. Built using **Python / Django** and styled with a customized, interactive, Accenture-inspired design language.

## 🚀 Key Features

*   **Premium Visual Experience**: Neon cyan & purple accents, glassmorphic panels, grid overlay, and high-performance background particle system.
*   **Accenture-Inspired Scroll Reveals**: Staggered content fade-ins, slide-ins, and numbers count-up triggered by scroll intersection observer.
*   **Fully Reskinned Django Admin**: Customized dark theme for the backend administrative terminal matching the public website aesthetics.
*   **Dynamic Sections**: Careers listings, Project grid category filters, and Client testimonials are all managed dynamically from the admin dashboard.
*   **Secure Contact Engine**: Built-in Django CSRF verification, input sanitization, and rate-limiting (3 submissions per minute) with AJAX submissions.

---

## 🛠️ Tech Stack & Dependencies

*   **Backend**: Python 3.13 / Django 6.0
*   **Frontend**: Django Template Language, Vanilla CSS, Vanilla JavaScript, Canvas API
*   **Production Server**: Gunicorn & WhiteNoise (static files compressor)
*   **Database**: SQLite (Development) / PostgreSQL (Production)
*   **Deployment**: Railway / Heroku (ready with `Procfile` & `runtime.txt`)

---

## 💻 Local Setup & Development

### 1. Prerequisites
Ensure you have **Python 3.12+** installed on your system.

### 2. Clone and Setup Environment
Open your shell in the project root:

```powershell
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
.\venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Run Migrations & Setup Admin
```powershell
# Make and apply migrations
python manage.py makemigrations
python manage.py migrate

# Local testing superuser is already pre-configured:
# Username: admin
# Password: AdminPasswordEscTrix2026
```

If you need to create a new custom superuser:
```powershell
python manage.py createsuperuser
```

### 4. Run Development Server
```powershell
python manage.py runserver
```
Visit the local site at: [http://127.0.0.1:8000](http://127.0.0.1:8000)
Visit the secure admin panel at: [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)

---

## 🛡️ Production Security & Railway Deployment

### 1. Database Provisioning
Railway automatically provisions a PostgreSQL database and injects `DATABASE_URL`. Django is configured via `dj-database-url` to automatically switch databases in production.

### 2. Set Environment Variables
In your Railway project settings, add the following variables:
*   `DEBUG`: `False`
*   `SECRET_KEY`: `your-random-production-secret-key`
*   `ALLOWED_HOSTS`: `your-railway-domain.up.railway.app`

### 3. Static Assets Compressing
`WhiteNoise` handles static files directly on Gunicorn. Before running, collect assets using:
```bash
python manage.py collectstatic --noinput
```
*(Railway runs this automatically during the build phase via Procfile config)*
