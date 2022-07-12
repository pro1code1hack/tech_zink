from models.models import Event


class EventService:
    """
    Creating the functions which gets data from the database according to the rest logic
    """

    @staticmethod
    def fetch_all_events(session):
        """
        Here we get all events from the database using SQLALCHEMY
        :param session:  current session of the db
        :return: all events
        """
        return session.query(Event)
