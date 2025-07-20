# 🔐 API-Based Auth System (Signup / Signin / Signout) – Django + JWT

A simple RESTful authentication system using Django REST Framework and Simple JWT.

---

## 🚀 Features

- ✅ User Signup (Register)
- ✅ User Signin (Login) with JWT
- ✅ User Signout (Blacklist Refresh Token)
- ✅ Token Refresh endpoint
- ✅ Secured routes using JWT

---

## 🛠️ Tech Stack

- Python 3.x
- Django
- Django REST Framework
- djangorestframework-simplejwt

---

## 📦 Installation

```bash
git clone "https://github.com/ammarproficient/api-based-signup-signin-signout.git"
cd pro
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
python manage.py migrate
python manage.py runserver
