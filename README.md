📚 Campus Connect

Campus Connect is a web-based platform built using Python Flask, SQLAlchemy, HTML, CSS, and JavaScript that connects students, clubs, and leaders in a college environment. It provides a centralized place to manage clubs, events, news, and activities.

🚀 Features
👨‍🎓 Students

View club descriptions, news, and events

Send join requests to clubs

Give feedback to clubs

Participate in club activities (after joining)

Receive in-app notifications for updates

🧑‍💼 Club Leaders

Edit club description

Add news and events

Upload photos (gallery)

View and respond to feedback

Accept or reject join requests

Add and manage club-specific activities

👩‍💻 Admin

Add new students (via CSV upload)

Create and delete clubs

Assign leaders from existing students

Oversee overall club activities

🗄️ Database Schema

The project uses a MySQL database with the following key tables:

students – Student details

club_leaders – Club leaders with assigned clubs

clubs – Club details (leader, coordinator, description, etc.)

club_members – Membership info linking students and clubs

news – Club-related news

events – Events with details and photos

⚙️ Technology Stack

Backend: Python Flask, SQLAlchemy

Frontend: HTML, CSS, JavaScript

Database: MySQL

Notifications: In-app alerts (no external mail service)

📂 Project Structure
Campus-Connect/
│── app.py              # Main Flask application  
│── models.py           # SQLAlchemy models  
│── static/             # CSS, JS, images  
│── templates/          # HTML templates  
│── uploads/            # Gallery uploads  
│── requirements.txt    # Dependencies  
│── README.md           # Documentation  

▶️ Installation & Setup

Clone the repository

git clone https://github.com/your-username/Campus-Connect.git
cd Campus-Connect


Create a virtual environment

python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows


Install dependencies

pip install -r requirements.txt


Configure Database

Open app.py (or config.py if separated).

Update the MySQL URI with your database name, username, and password:

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://username:password@localhost/college_connect'


Example:

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:mypassword@localhost/college_connect'


Setup MySQL database

Create a database named college_connect:

CREATE DATABASE college_connect;


Import the provided schema (or let SQLAlchemy create it automatically).

Run the Flask app

flask run


Open in browser → http://127.0.0.1:5000
