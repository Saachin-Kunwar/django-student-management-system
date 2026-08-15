# 🎓 Student Management System (Django)

A full-stack, responsive web application built with Python, Django, SQLite, and Bootstrap 5. This project was developed following professional software engineering workflows, implementing clean CRUD operations, dynamic search filtering, and robust server-side form validations.

---

## 🚀 Features

* **Dashboard & Directory:** View all registered students in an interactive data table.
* **Full CRUD Functionality:**
  * **Create:** Add new students using Django `ModelForm` with automatic field validation.
  * **Read:** Access detailed profile views for individual students.
  * **Update:** Pre-filled edit forms to safely update student information.
  * **Delete:** Modal confirmation to prevent accidental data deletion.
* **Search & Filtering:** Real-time query search across `name`, `email`, and `course` fields using Django ORM `Q` objects.
* **User Feedback:** Flash notification messages for user actions (create, edit, delete).
* **Responsive UI:** Built with Bootstrap 5 to ensure a clean layout on desktop and mobile screens.

---

## 🛠 Tech Stack

* **Backend:** Python 3.12, Django 5.x
* **Database:** SQLite3
* **Frontend:** HTML5, CSS3, Bootstrap 5, Django Template Language (DTL)
* **Version Control:** Git, GitHub

---

## 📂 Project Structure

```text
student_management/
├── config/                  # Project configuration & settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── students/                # Main Django Application
│   ├── templates/students/  # HTML Templates with Template Inheritance
│   │   ├── base.html
│   │   ├── student_confirm_delete.html
│   │   ├── student_detail.html
│   │   ├── student_form.html
│   │   └── student_list.html
│   ├── admin.py             # Admin interface configuration
│   ├── forms.py             # Django ModelForms
│   ├── models.py            # Database schema definition
│   ├── urls.py              # App-level routing
│   └── views.py             # Function-Based Views (FBVs) logic
├── .gitignore               # Excluded files (venv, db.sqlite3, cache)
├── manage.py
└── requirements.txt         # Project dependencies