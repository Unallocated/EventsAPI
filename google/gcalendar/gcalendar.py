import google.auth.authenticate
import json

calId = 'primary' 
scope = 'https://www.googleapis.com/auth/calendar'

event = {
    'summary': 'hackathon',
    'location': 'UAS',
    'start': {
        'dateTime': '2014-11-09T15:30:00.000-00:00',
        'timeZone': 'America/New_York'
        },
    'end': {
        'dateTime': '2014-11-10T15:30:00.000-00:00',
        'timeZone': 'America/New_York'
        },
    'attendees': [
        {
            'email': '0x9090cd80@gmail.com',
            }
        ]
    }

eventUpdate = {
    'summary': 'hackathon',
    'location': 'BWI',
    'start': {
        'dateTime': '2014-11-12T15:30:00.000-00:00',
        'timeZone': 'America/New_York'
        },
    'end': {
        'dateTime': '2014-11-12T16:00:00.000-00:00',
        'timeZone': 'America/New_York'
        },
    'attendees': [
        {
            'email': '0x9090cd80@gmail.com',
            }
        ]
    }

service = authenticate.authenticate(app, version, scope, user)

def create_event(event_body, notify=False):
    """
        Needed fields:
            summary, start, end, desc, location, recurrence
    """
    event = service.events().insert(calendarId=calId, body=event_body).execute()
    return event['id']

def delete_event(evtId, notify=False):
    service.events().delete(calendarId=calId, eventId=evtId, sendNotifications=notify)

def delete_events(eventIdList, notify=False):
    for evtId in eventIdList:
        service.events().delete(calendarId=calId, eventId=evtId, sendNotifications=notify)

def update_event(evtId, event_body, notify=False):
    return service.events().update(calendarId=calId, eventId=evtId, body=event_body, sendNotifications=notify).execute()

def get_event(evtId):
    return service.events().get(calendarId=calId, eventId=evtId).execute()

if __name__ == '__main__':

    # create an event
    evtid = create_event(event)
    print(evtid)

    # get and print the event data
    eventData = get_event(evtid)
    print(json.dumps(eventData))

    # test updating event
    uEventData = update_event(evtid, eventUpdate, True)
    uevtid = uEventData['id']
    eventData = get_event(uevtid)
    print(json.dumps(eventData))

    # delete events
    delete_event(evtid, True)
    delete_event(uevtid, True)
