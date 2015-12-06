import authenticate

class UASCalendar:
    __calendar_id = 'primary'
    __service = authenticate.authenticate('calendar', 'v3', 'https://www.googleapis.com/auth/calendar')
    
    def create_event(self, event_body, notify=False):
        event = self.__service.events().insert(calendarId=self.__calendar_id, body=event_body.obj).execute()
        return event

    def delete_event(event_id, notify=False):
        self.__service.events().delete(calendarId=self.__calendar_id, eventId=event_id, sendNotifications=notify)

    def delete_events(event_id_list, notify=False):
        for eventt_id in event_id_list:
            self.__service.events().delete(calendarId=self.__calendar_id, eventId=event_id, sendNotifications=notify)

    def update_event(self, event_id, event_body, notify=False):
        return self.__service.events().update(calendarId=self.__calendar_id, eventId=event_id, body=event_body, sendNotifications=notify).execute()


class EventBody:
	
	def __init__(self, summary, description, startTime, endTime, recurrances=None):
		obj = {
			'summary' : summary,
			'location' : '501 Shaw Ct',
			'description' : description,
			'start' : {
        'dateTime': startTime
			},
			'end' : {
        'dateTime': endTime
			}
		}

		self.obj = obj

	def getSummary(self):
		return self.obj['summary']

	def getDescription(self):
		return self.obj['description']

	def getStartTime(self):
		return self.obj['startTime']

	def getEndTime(self):
		return self.obj['endTime']

	def getRecurrances(self):
		return self.obj['recurrances']

	def hasRecurrances(self):
		return not self.obj['recurrances'] == None
	
	def getObj(self):
		print "OBJ: ",self.obj 
		return self.obj


if __name__ == "__main__":
    a = {
            "end": {
                'dateTime': "2015-12-05T23:00:00",
                "timeZone": 'UTC'
            },
            "start": {
                'dateTime': "2015-12-05T18:00:00",
                "timeZone": 'UTC'
            },
            "calendarId": 'uas.events.tester@gmail.com',
            "summary": 'moo cow',
            "description": 'just a test',
            "location": '1234'
        };

    api = UASCalendar()
    api.create_event(a)
