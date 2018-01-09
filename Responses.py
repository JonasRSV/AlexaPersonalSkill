
class WIERD_SHIT(object):
    """Keep stuff i don't understand but i think has to be there here."""
    EMPTY_REPROMPT = { "outputSpeech": { "type": "PlainText", "text": "null" }



class AUDIO_DIRECTIVES(object):
    """Class for audio directives."""

    STOP = {"type": "AudioPlayer.Stop"}

    def START(url):
        """Return directive for starting song at specific url."""
        return {
            "type": "AudioPlayer.Play",
            "playBehavior": "REPLACE_ALL",
            "audioItem": {
                    "stream": {
                        "token": "not sure what this is for tbh",
                        "url": url,
                        "offsetInMilliseconds": 0
                    }
            }
        }


def build_responselet(speech, reprompt, directives, shouldSessionEnd):
    """Build a responselet for the response."""
    return {
        "outputSpeech": {
            "type": "PlainText",
            "text": speech
        },
        "reprompt": reprompt,
        "directives": directives,
        "shouldSessionEnd": shouldSessionEnd
    }


def build_response(sessionAttributes, response):
    """Build a response in the expected format for Alexa."""
    return {
        "version": "1.0",
        "sessionAttributes": sessionAttributes,
        response: response
    }

