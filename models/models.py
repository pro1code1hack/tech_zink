import base64
import uuid
from database import db
from datetime import datetime

"""
**Ticket** db Structure:

- uuid 
- validity date
- status (OPTIONS: OK/Redeemed)
- Event -->FK 

**Event** db Structure:

- uuid 
- name VC
- date DATE
- number_of_tickets --> Relationship many to many to the model Ticket

(it must me calculated via agregations) 
"""


class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    number_of_tickets = db.Column(db.Integer, nullable=False)
    tickets = db.relationship('Ticket', backref='event', lazy=True)

    def __init__(self, name, date, number_of_tickets):
        self.name = name
        self.date = date
        # self.number_of_tickets = number_of_tickets

    def __repr__(self):
        return f"Event('{self.name}'),({self.date}), ({self.number_of_tickets})' "


class Ticket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.String(36), unique=True, nullable=False)
    validity_date = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(20), nullable=False)
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'), nullable=False)
    event = db.relationship('Event', backref='tickets', lazy=True)

    def __init__(self, uuid, validity_date, status, event_id):
        self.uuid = uuid
        self.validity_date = validity_date
        self.status = status
        self.event_id = event_id

    def __repr__(self):
        return f"Ticket('{self.uuid}'),({self.validity_date}), ({self.status}), ({self.event_id})' "
