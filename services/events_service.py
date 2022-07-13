from models.models import Event


class EventService:
    """
    Creating the functions which gets data from the database according to the rest logic
    Here we get all events from the database using SQLALCHEMY
    """

    @staticmethod
    def fetch_all_events(session):
        """
        :param session:  current session of the db
        :return: all events
        """
        return session.query(Event)

    @staticmethod
    def fetch_event_by_id(session, event_id):
        """
        :param session:  current session of the db
        :return: event by id
        """
        return session.query(Event).filter(Event.id == event_id).first()

    @staticmethod
    def fetch_last_event(session):
        """
        :param session: current session of the db
        :return: last event
        """
        return session.query(Event).order_by(Event.id.desc()).first()  # .id
