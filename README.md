
# 🛠 Schedulo – Django Service Booking App

A **simple, secure, and responsive** service booking application built with Django. It allows users to post services and customers to book them. Includes authentication, booking management, and admin control — **no Django REST Framework (DRF)**.

🌐 **Live Demo**: [https://schedulo-qg6d.onrender.com](https://schedulo-qg6d.onrender.com)

---

## 🌟 Features

### 👥 User Authentication
- Register, login, logout
- Secure password hashing and session-based login

### 🧾 Service Management
- Add/view/delete services (with price & duration)
- Track booking status: `Pending`, `Accepted`, `Rejected`, `Completed`

### 📅 Booking System
- Book a service by choosing a date
- Customers can view their bookings
- Providers can manage bookings

### 🛡 Admin Panel
- Superuser can:
  - Manage users
  - Oversee bookings and services
- Built-in Django Admin styled via static files

---

## 🛠 Tech Stack

- **Backend**: Django
- **Frontend**: Bootstrap 5 + Django Templates
- **Database**: SQLite (local), PostgreSQL (production)
- **Hosting**: Render
- **Static Serving**: WhiteNoise

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/service-booking.git
cd service-booking
```

### 2. Create & Activate Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scriptsctivate
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

### 4. Setup the Database

```bash
python manage.py migrate
```

### 5. Create a Superuser

```bash
python manage.py createsuperuser
```

### 6. Collect Static Files

```bash
python manage.py collectstatic
```

### 7. Run the Server

```bash
python manage.py runserver
```

Visit: [https://schedulo-qg6d.onrender.com](https://schedulo-qg6d.onrender.com)

---

## 🔧 Render Deployment Notes

### Build Command

```bash
python manage.py collectstatic --noinput
```

### Add to `MIDDLEWARE` in `settings.py`

```python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    ...
]
```

### Set Static File Storage

```python
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
```

### Environment Variables

- `SECRET_KEY`
- `DEBUG`
- `ALLOWED_HOSTS`
- `DATABASE_URL` (if using PostgreSQL)

---

## 📁 Directory Structure

```
schedulo/
├── manage.py
├── requirements.txt
├── service_booking/       # Project Settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── service_app/           # Booking Application
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── templates/
│   └── urls.py
├── static/                # Static Files
└── templates/             # Global Templates
```

---

## 🙌 Contributing

Contributions welcome! For major changes, open an issue first.

---

## 📜 License

Licensed under the [MIT License](https://opensource.org/licenses/MIT).

## 🪧 Demonstration



https://github.com/user-attachments/assets/48e8bc8f-b8bf-40bf-9f85-9b1df4aeb0ea


