import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://#username:#password@localhost/#database_name'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
