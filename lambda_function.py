
import thinglets
"""Thinglets, constants such and greetings, farewells and other stuff"""

import responses as response


class REQUEST_TYPE(object):
    """Alexa Request Types."""

    START_INTERACTION = "LaunchRequest",
    INTENT = "IntentRequest"


class INTENT_HANDLERS(object):
    """Alexa Intents."""

    STOP = "AMAZON.StopIntent"
    HitIt = "HitIt"
    Conversation = "Conversation"

    handlers = {
                STOP: INTENT_HANDLERS.stop_handler,
                HitIt: INTENT_HANDLERS.play_handler,
                Conversation: conversation_handler
              }


    def handle(intent, event):
        """Direct intents to corresponding handler"""
        if intent in INTENT_HANDLERS.handlers:
            return INTENT_HANDLERS.handlers[intent]()
        else:
            return INTENT_HANDLERS.unknown_handler()

    def stop_handler():
        """Handle stop intents."""
        should_session_end = True
        return response
                .build_response({},
                               response.build_responselet(
                                   thinglets.Farewell.getRandom(),
                                   response.REPROMPTS.EMPTY_REPROMPT,
                                   [response.AUDIO_DIRECTIVES.STOP],
                                   should_session_end))

    def play_handler():
        """Handle play intents such as starting music."""
        should_session_end = True
        return response
                .build_response({},
                               response.build_responselet(
                                   thinglets.Songs.getRandomResponseMaybe(),
                                   response.REPROMPTS.EMPTY_REPROMPT,
                                   [response.AUDIO_DIRECTIVES.START(
                                       thinglets.Songs.getRandomSong())],
                                   should_session_end))

    def conversation_handler():
        """Handle conversation intents."""
        should_session_end = False
        return response
                .build_response({},
                                response.build_responselet(
                                    thinglets.Conversation.getRandom(),
                                    response.REPROMPTS.REPROMPT("What does this do?"),
                                    [],
                                    should_session_end))

    def unknown_handler():
        """Handle unknown intents."""
        should_session_end = True
        return response
                .build_response({},
                               response.build_responselet(
                                   "Sir here's the anthem",
                                   response.REPROMPTS.EMPTY_REPROMPT,
                                   [response.AUDIO_DIRECTIVES.START(
                                       thinglets.Songs.RUSSKI)],
                                   should_session_end))

# Response handlers for all different kinds of responses alexa might send

def crash_handler():
    """Handle crashes."""
    should_session_end = True
    return response
            .build_response({},
                           response.build_responselet(
                               "Sir, You've written bad code, it crashed",
                               response.REPROMPTS.EMPTY_REPROMPT,
                               [],
                               should_session_end))


def unknown_request_handler():
    """Handle unknown requests."""
    should_session_end = True
    return response
            .build_response({},
                           response.build_responselet(
                               thinglets.Farewell.getRandom(),
                               response.REPROMPTS.EMPTY_REPROMPT,
                               [],
                               should_session_end))


def session_initializer():
    """Initialize a interaction between Alexa and User."""
    should_session_end = False
    return response.build_response({},
                                   response.build_responselet(
                                       thinglets.Greeting.getRandom(),
                                       response.REPROMPTS.EMPTY_REPROMPT,
                                       [],
                                       should_session_end))


def lambda_handler(event, context):
    """Entry point where requests is recieved and handled."""
    try:
        request_type = event["request"]["type"]

        if request_type == REQUEST_TYPE.START_INTERACTION:
            return session_initializer()
        elif request_type == REQUEST_TYPE.INTENT:
            return INTENT_HANDLERS.handle(event["request"]["intent"]["name"], event)
        else:
            return unknown_request_handler()
    except Exception:
       return crash_handler()

