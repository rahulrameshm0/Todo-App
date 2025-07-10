# 🗂️ Django Task Manager

A feature-rich and user-friendly Task Manager web application built using **Django**. This app allows users to efficiently manage daily tasks with priorities, due dates, and completion tracking.

---

## 📌 Project Overview

This Task Manager application is designed to help users:

- ✅ Add tasks with a name, priority level, and due date
- ✏️ Edit or update existing tasks
- ❌ Delete tasks no longer needed
- 📥 Mark tasks as completed via a checkbox
- 📋 View completed tasks separately
- 🔍 Filter tasks based on priority levels (High, Medium, Low)

It offers a clean and intuitive interface, with backend logic handled by Django and a responsive frontend using HTML and CSS.

---

## 🛠️ Tech Stack

| Layer     | Technology         |
|-----------|--------------------|
| Backend   | Django (Python)    |
| Frontend  | HTML5, CSS3        |
| Database  | SQLite (Default in Django) |
| Auth      | Django’s Built-in User Authentication |
| Deployment | Localhost (Runserver) |

---

## 🧩 Features Breakdown

- **User Authentication** – Login/Signup using Django's built-in auth
- **Task Management**:
  - Create tasks with specific priority and due date
  - Update task details anytime
  - Delete tasks instantly
- **Completion Toggle**:
  - Checkbox to mark a task as complete
  - Moves task from active list to a separate completed section
- **Filter Options**:
  - Filter tasks by High, Medium, or Low priority
  - Easy navigation with filter links
- **Dynamic UI Updates**:
  - Automatically hides completed tasks from active list
  - Updates without reloading whole form
- **Secure CSRF Protection**:
  - Every form submission includes CSRF tokens for security

---

## 🚀 Getting Started

### 1. Clone the repository

git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

2. Set up a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
3. Install dependencies
pip install -r requirements.txt
4. Run migrations
python manage.py migrate
5. Start the development server
python manage.py runserver
6. Open in browser
Visit http://127.0.0.1:8000 to view the app.

## 📂 Project Structure

/project-root
│
├── taskmanager/           # Main Django App
│   ├── templates/         # HTML templates (login, signup, todo)
│   ├── static/            # CSS files
│   ├── models.py          # Task model
│   ├── views.py           # All logic handled here
│   ├── urls.py            # Route mapping
│   └── forms.py           # (if used) Django forms
│
├── db.sqlite3             # Default database
├── manage.py              # Django CLI tool
└── requirements.txt       # List of dependencies


## 👨‍💻 Author
Developed by Rahul
GitHub: @rahulrameshm0

## 🗣️ Contribute
Want to contribute? You’re welcome!
Feel free to fork the repo and raise a pull request.





