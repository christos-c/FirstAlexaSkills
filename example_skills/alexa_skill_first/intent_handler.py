from helpers import build_response, build_speechlet_response


class IntentHandler:
    def __init__(self, mappings):
        self.intent_mappings = mappings

    def intent_handler(self, intent, session):
        """
        Collects values to generate an Alexa response
        by calling custom logic based on the intent name
        """
        session_attributes = {}
        should_end_session = True
        reprompt_text = "i didn't get that please repeat"

        intent_name = intent['name']
        if intent_name in self.intent_mappings:
            if 'slots' not in intent:
                slots = {}
            else:
                slots = intent['slots']
            speech_output = self.intent_mappings[intent_name](slots)
        else:
            # this shouldn't occur unless we omit the implementation of some intent
            should_end_session = True
            speech_output = "hmm not sure how to deal with your request"

        speechlet_response = build_speechlet_response(intent['name'], speech_output, reprompt_text, should_end_session)
        return build_response(session_attributes, speechlet_response)
