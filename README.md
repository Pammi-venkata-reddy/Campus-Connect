Campus Connect

Campus Connect is a Flask-based web application designed to manage and collaborate across college clubs. Each club has its own section where admins can post news, events, and media, while students can engage with content and provide feedback.

Features

Flask backend with SQLAlchemy ORM

Club management: admins can post updates, events, and announcements

Student engagement: feedback and interactions

Modular structure with templates and static files

Easy database setup using models.py

Tech Stack

Backend: Flask, SQLAlchemy

Frontend: HTML, CSS, JavaScript

Database: SQLite (default)

Getting Started
1. Clone the Repository
git clone https://github.com/Pammi-venkata-reddy/Campus-Connect.git
cd Campus-Connect

2. Create and Activate Virtual Environment
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Linux/Mac:
source venv/bin/activate

3. Install Dependencies
pip install -r requirements.txt

4. Initialize the Database

Inside your project folder:

python
>>> from app import db
>>> db.create_all()
>>> exit()


(This will create the database tables defined in models.py)

5. Run the Application
python run.py


Then open: http://127.0.0.1:5000/

Project Structure
Campus-Connect/
│── app/
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   ├── templates/
│   └── static/
│── config.py
│── run.py
│── requirements.txt
│── .gitignore
