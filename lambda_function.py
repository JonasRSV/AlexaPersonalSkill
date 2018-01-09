import Thinglets
import Responses as Response


class REQUEST_TYPE(object):
    """Alexa Request Types."""

    START_INTERACTION = "LaunchRequest",
    INTENT = "IntentRequest"

class INTENT_HANDLERS(object):
    """Alexa Intents."""

    STOP = "AMAZON.StopIntent"

    def stop_handler():
        """Handle stop intents."""
        should_session_end = True
        return Response.build_response({},
                                       Response.build_responselet(
                                           Thinglets.Farewell.getRandom(),
                                           Response.WIERD_SHIT.EMPTY_REPROMPT,
                                           [Response.AUDIO_DIRECTIVES.STOP],
                                           should_session_end))

    def unknown_handler():
        """Handle unknown intents."""
        should_session_end = True
        return Response.build_response({},
                                       Response.build_responselet(
                                           "Sir here's the anthem",
                                           Response.WIERD_SHIT.EMPTY_REPROMPT,
                                           [Response.AUDIO_DIRECTIVES.START(
                                               Thinglets.Songs.RUSSKI)],
                                           should_session_end))


def crash_handler():
    """Handle crashes."""
    should_session_end = True
    return Response.build_response({},
                                   Response.build_responselet(
                                       "Sir, You've written bad code, it crashed",
                                       Response.WIERD_SHIT.EMPTY_REPROMPT,
                                       [],
                                       should_session_end))


def unknown_request_handler():
    """Handle unknown requests."""
    should_session_end = True
    return Response.build_response({},
                                   Response.build_responselet(
                                       Thinglets.Farewell.getRandom(),
                                       Response.WIERD_SHIT.EMPTY_REPROMPT,
                                       [],
                                       should_session_end))


def intent_handler(event):
    """Handle intent."""
    intent = event["request"]["intent"]["name"]

    if intent is INTENT_HANDLERS.STOP:
        return INTENT_HANDLERS.stop_handler()
    else:
        return INTENT_HANDLERS.unknown_handler()


def session_initializer():
    """Initialize a interaction between Alexa and User."""
    should_session_end = False
    return Response.build_response({},
                                   Response.build_responselet(
                                       Thinglets.Greeting.getRandom(),
                                       Response.WIERD_SHIT.EMPTY_REPROMPT,
                                       [],
                                       should_session_end))



def lambda_handler(event, context):
    """Entry point where requests is recieved and handled."""

    try:
        request_type = event["request"]["type"]

        if request_type == REQUEST_TYPE.START_INTERACTION:
            return session_initializer()
        elif request_type == REQUEST_TYPE.INTENT:
            return intent_handler(event)
        else:
            return unknown_request_handler()
    except Exception:
        return crash_handler()



        




