import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:Venkat%4014@localhost/college_connect'
    SQLALCHEMY_TRACK_MODIFICATIONS = False