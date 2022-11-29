
from flask_sqlalchemy import SQLAlchemy

from app import db


class Blogs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable = False)
    body = db.Column(db.String(400), nullable = False)
    author = db.Column(db.String(100), nullable = False)
