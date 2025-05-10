# 🛠 Schedulo App

Schedulo is a Django-based web app for managing and booking services with role-based access for service providers and customers.

🌐 **Live Demo**: [schedulo-qg6d.onrender.com](https://schedulo-qg6d.onrender.com)

---

## 🚀 Features

### 👥 Authentication
- User Registration, Login, and Logout
- Role-based dashboard (Service Provider / Customer)

### 🧾 Service Management
- **Add New Service**: Add name, description, price, estimated time.
- **View/Delete Services**: Manage your posted services.
- **Change Booking Status**: Set status to Pending, Accepted, Rejected, or Completed for services you own.

### 📅 Booking System
- Book services for a specific date.
- Track your bookings.
- View requests for services you own and manage their statuses.

### 🛡 Admin Panel
- Manage users, services, and bookings via Django admin.

---

## 🛠 Tech Stack

- **Backend**: Django 5.1.5
- **Frontend**: HTML5, CSS, Bootstrap 5
- **Database**: PostgreSQL (via `dj-database-url`)
- **Hosting**: Render.com

---

## 📦 Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/service-booking-app.git
cd service-booking-app
```

### 2️⃣ Create and Activate Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate     # On Windows: .venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Set Environment Variables

Create a `.env` file in the project root:

```
SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
DATABASE_URL=your-postgres-database-url
```

### 5️⃣ Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6️⃣ Create Superuser

```bash
python manage.py createsuperuser
```

### 7️⃣ Run the Development Server

```bash
python manage.py runserver
```

Visit: [https://schedulo-qg6d.onrender.com](https://schedulo-qg6d.onrender.com)

---

## 🚀 Deployment (Render)

- **Set Environment Variables** in the Render dashboard:
  - `SECRET_KEY`
  - `DEBUG=False`
  - `ALLOWED_HOSTS=schedulo-qg6d.onrender.com`
  - `DATABASE_URL`

- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `gunicorn service_booking.wsgi:application`

- Add `staticfiles` configuration in Render:
  - `STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')`
  - Use `WhiteNoise` for static file serving.

---

## 🧪 How to Use

### As a Customer
- Register and log in.
- Browse and book services.
- View and track your bookings.

### As a Service Provider
- Log in and add your services.
- View booking requests.
- Update booking statuses.
- Delete your services if needed.

---

## 📄 License

This project is licensed under the MIT License.

---

## 🤝 Contributing

Pull requests and issues are welcome!
