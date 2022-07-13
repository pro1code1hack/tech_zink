"""
Write the code which will create a lot of instances to the db in Event and Ticket tables
"""
from models.models import Event, Ticket
from database import db
import datetime
import uuid


def create_events(session):
    """
    Here we create a lot of events to the db
    :param session:  current session of the db
    :return: None
    """
    for i in range(10):
        event = Event(
            name="Event {}".format(i),
            number_of_tickets=2 * i
        )
        session.add(event)
    session.commit()


def create_tickets(session):
    """
    Here we create a lot of tickets to the db
    :param session:  current session of the db
    :return: None
    """
    for i in range(10):
        ticket = Ticket(
            event_id=i,
            status="OK"
        )
        session.add(ticket)
    session.commit()
