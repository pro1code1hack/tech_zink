from models.models import Ticket


class TicketService:
    """
    Creating the functions which gets data from the database according to the rest logic
    """
    @staticmethod
    def fetch_all_tickets(session):
        """
        Here we get all tickets from the database using SQLALCHEMY
        :param session:  current session of the db
        :return: all tickets
        """
        return session.query(Ticket)