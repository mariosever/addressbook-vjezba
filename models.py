import os
from sqla_wrapper import SQLAlchemy

db = SQLAlchemy(os.getenv("DATABASE_URL", "sqlite:///localhost.sqlite"), connect_args={"check_same_thread": False})

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=False)
    address = db.Column(db.String, unique=False)
    phone = db.Column(db.String, unique=True)
    email = db.Column(db.String, unique=True)