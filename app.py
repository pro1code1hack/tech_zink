import http
import logging
import random
import sys
import uuid

from flask import Flask, request
from flask_migrate import Migrate
import os
from flask_restful import Api, Resource
from flask_swagger_ui import get_swaggerui_blueprint
from flask import Response
from database import db
from models.models import Ticket, Event
# It is essential to import the models here, otherwise the alembic will not be able to find them
# from rest.events import EventsApi
from services.events_service import EventService
from services.tickets_service import TicketService
from validators.api_validation import validate_post_json

basedir = os.path.abspath(os.path.dirname(__file__))


# =======================================================================================================================#
class EventsApi(Resource):

    def get(self, uuid=None):
        serialized_events = []  # creating a list to store the serialized events
        events = EventService.fetch_all_events(db.session)  # getting all events from the database
        for event in events:
            serialized_events.append(event.to_dict())  # here we are serializing the events
        return serialized_events, 200

    def post(self):
        """
        Request json data and adding new item to the database
        :return: 201 HTTP status code
        """
        validate_post_json(request.json)  # validating the json data
        post_json = request.json
        try:
            new_event = Event(**request.json)
        except (ValueError, KeyError) as e:
            return {'message': "Wrong data"}, 400
        db.session.add(new_event)
        db.session.commit()
        num_of_tickets = post_json.get('number_of_tickets')  # get the number of tickets from the json
        last_event = EventService.fetch_last_event(db.session).id  # getting the last event id
        print(last_event)
        for i in range(num_of_tickets):  # here we are generating the tickets for the last event
            ticket = Ticket(status=random.choice(['OK', 'Redeemed']), event_id=last_event)  # generating tickets
            db.session.add(ticket)
            db.session.commit()
        return 200

    # =======================================================================================================================#


class TicketsApi(Resource):
    def get(self, id):
        """
        Getting the ticket by id
        :param id: id of the ticket ( uuid by the default ps: I changed the default type of the id to uuid)
        :return: Responsse status code
        """
        ticket = TicketService.get_the_ticket_by_id(db.session, id)
        # return http response if the ticket status is ok
        return Response('OK', status=200) if ticket.status == 'OK' else Response('GONE', status=410)

    def post(self):
        """
        Request json data and adding new ticket to the database
        :return:
        """
        validate_post_json(request.json)  # validating the json data
        post_json = request.json
        try:
            # get the event id and status from the json
            event_id, status = post_json.get('event_id'), post_json.get('status')
            # check if the event exists in the db and if the status is chosen correct
            if not EventService.fetch_event_by_id(db.session, event_id) or status not in ['OK', 'Redeemed']:
                return {'message': "Event does not exist or status not in [OK/Redeemed]"}, 400
            new_ticket = Ticket(**request.json)  # creating a new instance of ticket
        except (ValueError, KeyError) as e:
            return {'message': "Wrong data"}, 400
        db.session.add(new_ticket)
        db.session.commit()  # saving the changes to the db
        return 200
    # =======================================================================================================================#


def create_app(db_location):
    """
    Function that creates our Flask application.
    This function creates the Flask app, Flask-Restful API,
    and Flask-SQLAlchemy connection
    :param db_location: Connection string to the database
    :return: Initialized Flask app
    """
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s %(name)-12s %(levelname)-8s %(message)s",
        datefmt="%m-%d %H:%M",
        handlers=[logging.FileHandler("api.log"), logging.StreamHandler()],
    )
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'                                                                   #TODO: use .env file
    app.config["SQLALCHEMY_DATABASE_URI"]=os.environ.get('DATABASE_URL') or 'sqlite:///'+os.path.join(basedir,'test.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    #app.config['SQLALCHEMY_ECHO'] = True

    from database import db

    # Initialize the database connection
    db.init_app(app)
    db.app = app
    migrate = Migrate(app, db)

    # bcrypt = Bcrypt(app)

    # swagger setup
    SWAGGER_URL = '/swagger'
    API_URL = '/static/swagger.json'

    SWAGGER_BLUEPRINT = get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL,
        config={
            'app_name': 'z1nc'
        }
    )
    app.register_blueprint(SWAGGER_BLUEPRINT, url_prefix=SWAGGER_URL)

    # creating the api itself
    api = Api(app)
    api.add_resource(EventsApi, '/events', '/events/<uuid>', strict_slashes=False)
    api.add_resource(TicketsApi, '/tickets', '/redeem/<id>', strict_slashes=False)
    return app


if __name__ == '__main__':
    app = create_app("site.db")
    app.run(debug=True, port=63535, host="0.0.0.0")
