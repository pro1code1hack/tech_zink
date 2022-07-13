from database import db
from models.models import Ticket


class TicketService:
    """
    Creating the functions which gets data from the database according to the rest logic
    Here we get all tickets from the database using SQLALCHEMY
    """

    @staticmethod
    def fetch_all_tickets(session):
        """
        :param session:  current session of the db
        :return: all tickets
        """
        return session.query(Ticket)

    @staticmethod
    def fetch_redeemed_tickets(session):
        """
        Here we get all tickets from the database using SQLALCHEMY
        :param session:  current session of the db
        :return: all tickets
        """
        return session.query(Ticket).filter(Ticket.status == 'Redeemed')

    @staticmethod
    def get_the_amount_of_red_tickets(session: db.session, event_id: int):
        return len(session.query(Ticket).filter(Ticket.event_id == event_id, Ticket.status == 'Redeemed'))

    @staticmethod
    def get_the_ticket_by_id(session: db.session, ticket_id: int):
        return session.query(Ticket).filter(Ticket.id == ticket_id).first()
