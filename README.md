# Flask Notes App

A simple web app where users can create an account, log in, and keep their own private notes. Built with Flask while learning web development.
**Live demo:** https://flask-notes-app-zvvm.onrender.com

## Features

- Sign up with validation (email, name, matching passwords, minimum password length)
- Passwords stored securely as hashes, never as plain text
- Login and logout with session handling
- Protected home page that only logged-in users can open
- Add, edit and delete personal notes (each user sees only their own)
- Responsive pages styled with Bootstrap and custom CSS

## Built with

- Python and Flask
- Flask-SQLAlchemy (SQLite database)
- Flask-Login
- HTML, Jinja2 templates, Bootstrap, CSS

## Run it locally

1. Clone the repository:
   ```
   git clone https://github.com/mikemichira-hue/flask-notes-app.git
   cd flask-notes-app
   ```
2. Install the dependencies:
   ```
   python -m pip install -r requirements.txt
   ```
3. Start the app:
   ```
   python main.py
   ```
4. Open `http://127.0.0.1:5000` in your browser.

## Project structure

```
flask-notes-app/
├── main.py
├── requirements.txt
└── website/
    ├── __init__.py   # app setup, database and login manager
    ├── models.py     # User and Note tables
    ├── auth.py       # login, logout and sign-up routes
    ├── views.py      # home page and note routes
    ├── static/       # CSS
    └── templates/    # HTML pages
```

## Author

Built by Micah Michira.
