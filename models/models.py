import base64
import uuid
from database import db
from datetime import datetime
from sqlalchemy.dialects.postgresql import UUID


class Event(db.Model):
    __tablename__ = "events"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    date = db.Column(db.Date, nullable=True, default=datetime.now())
    number_of_tickets = db.Column(db.Integer, nullable=False, default=10)
    tickets = db.relationship("Ticket", backref="event", lazy=True)

    def __init__(self, name, number_of_tickets):
        self.name = name
        self.number_of_tickets = number_of_tickets

    def to_dict(self):
        # The method is used for serializing the object to a dictionary
        return {
            "id": self.id,
            "name": self.name,
            "date": str(self.date),
            "number_of_tickets": self.number_of_tickets,
            "ok_tickets": len(list(filter(lambda ticket: ticket.status == "OK", self.tickets))),
            "redeemed_tickets": len(list(filter(lambda ticket: ticket.status == "Redeemed", self.tickets))),
            "tickets": [ticket.to_dict() for ticket in self.tickets]
        }


class Ticket(db.Model):
    __tablename__ = "tickets"

    # The following code is used for change the default column int (id) to UUID by default unique identifier

    id = db.Column('id', db.Text(length=36), default=lambda: str(uuid.uuid4()), primary_key=True)
    status = db.Column(db.String(80), nullable=False, default="OK")
    event_id = db.Column(db.Integer, db.ForeignKey("events.id"), nullable=False)

    def __init__(self, status, event_id):
        self.status = status
        self.event_id = event_id

    def to_dict(self):
        # The method is used for serializing the object to a dictionary
        return {
            "uuid": self.id,
            "status": self.status,
            "event_id": self.event_id
        }
