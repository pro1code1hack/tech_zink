# from importlib.resources import Resource
#
# from database import db
# from services.events_service import EventService
#
#
# class EventsApi(Resource):
#
#     def get(self, uuid=None):
#         if not uuid:
#             events = EventService.fetch_all_events(db.session)
#             print(events)
#             serialized_events = [event.__dict__() for event in events]
#             print(serialized_events)
#             return serialized_events, 200
#
