import logging
from enum import Enum


class EventType(Enum):
    ADDED_TO_SPACE = 'ADDED_TO_SPACE'
    MESSAGE = 'MESSAGE'
    CARD_CLICKED = 'CARD_CLICKED'
    REMOVED_FROM_SPACE = 'REMOVED_FROM_SPACE'


class SpaceType(Enum):
    ROOM = 'ROOM'
    DIRECT_MESSAGE = 'DM'


class UserType(Enum):
    HUMAN = 'HUMAN'
    BOT = 'BOT'


class HangoutsChatHandler:
    SpaceType = SpaceType
    EventType = EventType
    ActionMethod = Enum

    def __init__(self, logger=None, debug=False):
        if logger is None:
            logger = logging.getLogger(__name__)
        self.log = logger
        self.debug = debug

    def _parse_action_parameters(self, parameters):
        parsed_parameters = {}
        for p in parameters:
            key = p['key']
            value = p['value']
            parsed_parameters[key] = value
        return parsed_parameters

    def handle_chat_event(self, event, sent_asynchronously=False):
        try:
            self.sent_asynchronously = sent_asynchronously
            event_type = EventType(event['type'])
            space_type = SpaceType(event['space']['type'])
            if event_type == EventType.ADDED_TO_SPACE:
                response = self.handle_added_to_space(space_type, event=event)
            elif event_type == EventType.REMOVED_FROM_SPACE:
                response = self.handle_removed_from_space(space_type, event=event)
            elif event_type == EventType.CARD_CLICKED:
                action_method = self.ActionMethod(event['action']['actionMethodName'])
                parameters = event['action'].get('parameters', {})
                if parameters:
                    parameters = self._parse_action_parameters(parameters)
                response = self.handle_card_clicked(action_method, parameters, event=event)
            elif event_type == EventType.MESSAGE:
                message = event['message']
                response = self.handle_message(message, event=event)
        except Exception as e:
            logging.exception('Error handling chat event')
            response = self.handle_exception(e, event=event)
        return self.handle_response(response)

    def handle_response(self, response):
        return response

    def handle_exception(self, e, **kwargs):
        if self.debug:
            return {'text': str(e)}

    def handle_added_to_space(self, space_type, **kwargs):
        pass

    def handle_message(self, message, **kwargs):
        pass

    def handle_card_clicked(self, action_method, action_parameters, **kwargs):
        pass

    def handle_removed_from_space(self, space_type, **kwargs):
        pass
