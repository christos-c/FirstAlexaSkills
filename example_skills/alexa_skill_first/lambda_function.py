from helpers import *
import random

from intent_handler import IntentHandler


def get_something(slot):
    speech_output = "I say whatever I please"
    return speech_output


def get_coolest(slot):
    subject = slot['Subject']['value']

    coolest_dict = {"movie": ["Lord of the rings", "Batman, the dark knight", "Indiana Jones"]}
    if subject in coolest_dict:
        valid_answers = coolest_dict[subject]
        speech_output = random.choice(valid_answers)
    else:
        speech_output = "I don't know much about " + str(subject) + " yet"
    return speech_output


def get_person_fact(slot):
    """
    Finds a fact about a name
    """
    person_name = slot['Person']['value']
    if person_name.lower() == 'catherine':
        speech_output = 'catherine works at amazon building models for alexa'
    elif person_name.lower() == 'jason':
        speech_output = 'jason likes pies'
    else:
        speech_output = 'i don\'t know much about ' + person_name
    return speech_output


def get_end_time(slot):
    thing = slot['Thing']['value']

    times_dict = {"demo": "noon", "life": "too soon", "term": "too late", "winter": "never"}
    if thing in times_dict:
        time = times_dict[thing]
        speech_output = "the " + thing + " ends " + time
    else:
        speech_output = "I don't know when " + str(thing) + " ends"
    return speech_output

# --------------- Intent mappings ---------------
# The names in quotes need to match the intent names in the Alexa Developer console
# The names after the colons are the method names above (*without* parentheses)
intent_mappings = {
    'saySomethingIntent': get_something,
    'whatsCoolIntent': get_coolest,
    'personalFactIntent': get_person_fact,
    'whenDoesItEndIntent': get_end_time
}
intent_handler = IntentHandler(intent_mappings)


# --------------- Main handler ------------------
def lambda_handler(event, context):
    """ Route the incoming request based on type (LaunchRequest, IntentRequest,
    etc.) The JSON body of the request is provided in the event parameter.
    """
    print("event.session.application.applicationId=" + event['session']['application']['applicationId'])

    if event['session']['new']:
        on_session_started({'requestId': event['request']['requestId']}, event['session'])

    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'], intent_handler)
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'])
