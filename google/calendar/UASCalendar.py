import authenticate

class UASCalendar:
    __calendar_id = 'primary'
    __service = authenticate.authenticate('calendar', 'v3', 'https://www.googleapis.com/auth/calendar')
    
    def create_event(self, event_body, notify=False):
        event = self.__service.events().insert(calendarId=self.__calendar_id, body=event_body.obj).execute()
        print event.get('htmlLink')
        return event

    def delete_event(self, event_id, notify=False):
        self.__service.events().delete(calendarId=self.__calendar_id, eventId=event_id, sendNotifications=notify)

    def delete_events(self, event_id_list, notify=False):
        for eventt_id in event_id_list:
            self.__service.events().delete(calendarId=self.__calendar_id, eventId=event_id, sendNotifications=notify)
    
    def list_events(self):
        pageToken = None
        resp = self.__service.events().list(calendarId=self.__calendar_id, pageToken=pageToken).execute()
        for i in resp['items']:
            if 'end' in i and 'timeZone' in i['end'] and 'description' in i and 'htmlLink' in i:
                print '%s :::: %s :::: %s :::: %s :::: %s to %s' % (i['end']['timeZone'], i['description'], i['created'], i['htmlLink'], i['start']['dateTime'], i['end']['dateTime'])


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
    import datetime

    currentDate = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
    a = {
            "end": {
                'dateTime': currentDate,
                "timeZone": 'EST'
            },
            "start": {
                'dateTime': currentDate,
                "timeZone": 'EST'
            },
            "calendarId": 'uaas.events.tester@gmail.com',
            "summary": 'moo cow',
            "description": 'just a test',
            "location": '1234'
        };

    e = EventBody(summary='moo cow summary', description='moo cow description', startTime='2015-12-05T11:00:00', endTime='2015-12-05T12:00:00')
    api = UASCalendar()
    api.create_event(e)
