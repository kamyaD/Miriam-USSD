from app import db
from sqlalchemy.dialects.postgresql import JSON
from flask_sqlalchemy import SQLAlchemy



class Response(db.Model):
    __tablename__='response'

    id=db.Column(db.Integer, primary_key=True)
    order=db.Column(db.String())
    location = db.Column(db.String())
    phone = db.Column(db.String())

    def __init__(self, order, location, phone):
        self.order = order
        self.location = location
        self.phone = phone

    def __repr__(self):
        return '<id {}>'.format(self.id)

