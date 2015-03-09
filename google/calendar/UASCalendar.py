import authenticate

class UASCalendar:
    __calendar_id = 'primary'
    __service = authenticate.authenticate('calendar', 'v3', 'https://www.googleapis.com/auth/calendar')
    
    def create_event(self, event_body, notify=False):
        event = self.__service.events().insert(calendarId=self.__calendar_id, body=event_body).execute()
        print event
                #return event['id']

    def delete_event(self, event_id, notify=False):
        self.__service.events().delete(calendarId=self.__calendar_id, eventId=event_id, sendNotifications=notify)

    def delete_events(self, event_id_list, notify=False):
        for eventt_id in event_id_list:
            self.__service.events().delete(calendarId=self.__calendar_id, eventId=event_id, sendNotifications=notify)

    def update_event(self, event_id, event_body, notify=False):
        return self.__service.events().update(calendarId=self.__calendar_id, eventId=event_id, body=event_body, sendNotifications=notify).execute()


class EventBody:
    
    def __init__(self, summary, description, startTime, endTime, recurrances=None):
        obj = {
            'summary': summary,
            'description' : description,
            'location': 'UAS',
            'start': {
                'dateTime': startTime,
                'timeZone': 'America/New_York'
                },
            'end': {
                'dateTime': endTime,
                'timeZone': 'America/New_York'
                },
            'attendees': [
                {
                    'email': '0x9090cd80@gmail.com',
                    }
                ]
        }

        self.obj = obj

    def getSummary(self):
        return self.obj.summary

    def getDescription(self):
        return self.obj.description

    def getStartTime(self):
        return self.obj.startTime

    def getEndTime(self):
        return self.obj.endTime

    def getRecurrances(self):
        return self.obj.recurrances

    def hasRecurrances(self):
        return not self.obj.recurrances == None
    
    def getObj(self):
        print "OBJ: ",self.obj 
        return self.obj

if __name__ == "__main__":
    summary = 'my summary'
    description = 'Test calendar event 3/8/15'
    start = '2015-03-11T18:00:00.000-00:00'
    end = '2015-03-11T19:00:00.000-00:00'

    cal = UASCalendar()
    event = EventBody(summary, description, start, end)
    cal.create_event(event.getObj())
