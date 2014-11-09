import authenticate

calendarId = 'primary' 

event = {
    'summary': 'hackathon',
    'location': 'UAS',
    'start': {
        'dateTime': '2014-11-09T15:30:00.000-07:00',
        'timeZone': 'America/Los_Angeles'
        },
    'end': {
        'dateTime': '2014-11-10T15:30:00.000-07:00',
        'timeZone': 'America/Los_Angeles'
        },
    'attendees': [
        {
            'email': '0x9090cd80@gmail.com',
            }
        ]
    }


def create_event(summary, start, end, desc, location, sendNotifications=False, recurrence=None):
    """ create a calendar event. Returns the event ID """

    if (recurrence):
        event = service.events().insert(calendarId, body=event, sendNotifications).execute()
    else:
        event = service.events().insert(calendarId, body=event, sendNotifications).execute()

    print event
    return event['id']

def delete_event(eventId, sendNotifications=False):
    """ delete a calendar event. """
    service.events().delete(calendarId, eventId, sendNotifications)

def delete_events(eventIdList, sendNotifications=False):
    """ deletes a list of calendar events. """
    for eventId in eventIdList:
        service.events().delete(calendarId, eventId, sendNotifications)

def update_event(start, end, desc, location, sendNotifications=False):
    """update a calendar event. """
    service.events().insert(calendarId, body=event, sendNotifications=False).execute()

def get_event(eventId):
    """Retrieve a calendar event. """
    return service.events().insert(calendarId).execute()

service = authenticate.authenticate()

creat_event(

