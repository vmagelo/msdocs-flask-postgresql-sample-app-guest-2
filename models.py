from app import db
from sqlalchemy.dialects.postgresql import JSON

class Guest(db.Model):
    """Simple database model to track event attendees."""

    __tablename__ = 'guests2'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    email = db.Column(db.String(120))
    notes = db.Column(db.String(120))

    def __init__(self, name=None, email=None):
        self.name = name
        self.email = email