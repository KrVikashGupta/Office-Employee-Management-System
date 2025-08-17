<!-- Gradient Header -->
<h1 align="center">
  <span style="background: linear-gradient(90deg, #ff7e5f, #feb47b, #86a8e7, #91eae4); -webkit-background-clip: text; color: transparent;">
    🏢 Office Employee Management System
  </span>
</h1>

<p align="center">
  <img src="https://media.giphy.com/media/3oEjI6SIIHBdRxXI40/giphy.gif" alt="Office Animation" width="500"/>
</p>

<p align="center">
  <a href="https://www.python.org/">
    <img src="https://img.shields.io/badge/Python-3.13-blue?logo=python&logoColor=white" alt="Python"/>
  </a>
  <a href="https://www.djangoproject.com/">
    <img src="https://img.shields.io/badge/Django-5.2.4-green?logo=django&logoColor=white" alt="Django"/>
  </a>
  <a href="https://github.com/KrVikashGupta/Office-Employee-Management-System/issues">
    <img src="https://img.shields.io/github/issues/KrVikashGupta/Office-Employee-Management-System?color=yellow" alt="Issues"/>
  </a>
  <a href="LICENSE">
    <img src="https://img.shields.io/badge/License-MIT-blue" alt="License"/>
  </a>
</p>

---

## ✨ About
A **modern Django application** to manage employees efficiently. Track employee records, departments, roles, and documents—all in one place.  

<p align="center">
  <img src="https://media.giphy.com/media/xT5LMHxhOfscxPfIfm/giphy.gif" alt="Django App Demo" width="500"/>
</p>

---

## 🚀 Features
- 🎯 Add, update, and delete employees  
- 🏷️ Manage departments & roles  
- 📄 Upload/view documents & images  
- 🔑 Role-based authentication  
- 💾 Export data as CSV or PDF  
- 📱 Responsive and mobile-friendly  

---

## 🛠 Tech Stack
- **Backend:** Django 5.2.4, Python 3.13  
- **Database:** SQLite / PostgreSQL  
- **Frontend:** HTML, CSS, JS, Bootstrap  
- **Libraries:** Pillow, django-crispy-forms, requests, whitenoise  

---

## ⚡ Installation

```bash
# Clone repo
git clone https://github.com/KrVikashGupta/Office-Employee-Management-System.git
cd Office-Employee-Management-System/office_emp_proj

# Create virtual environment
python -m venv venv

# Activate venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run server
python manage.py runserver
