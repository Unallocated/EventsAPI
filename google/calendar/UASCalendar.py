from authenticate import GoogleAuthentication

class UASCalendar:
	__calendar_id = 'uas.events.tester@gmail.com'
	google = GoogleAuthentication("gauth.cfg")
	__service = google.authenticate(app="calendar", version='v3', scope='profile https://www.googleapis.com/auth/calendar')
	
	def create_calendar(self, calendarName):
		resp = self.__service.calendars().insert(body={'summary': calendarName, 'timeZone' : 'America/New_York'}).execute()
		return resp

	def list_calendars(self):
		page_token = None
		while True:
			calendar_list = self.__service.calendarList().list(pageToken=page_token).execute()
			print calendar_list
			for calendar_list_entry in calendar_list['items']:
				print calendar_list_entry["summary"]
				page_token = calendar_list.get('nextPageToken')
				print page_token
			if not page_token:
				break

	def get_calendar(self):
		calendar = self.__service.calendars().get(calendarId='uas.events.tester@gmail.com').execute()
		print calendar

	def create_event(self, event_body, notify=False):
		event = self.__service.events().insert(calendarId=self.__calendar_id, body=event_body.toJSON()).execute()
		print event.get('htmlLink')
		return event

	def delete_event(self, event_id, notify=False):
		self.__service.events().delete(calendarId=self.__calendar_id, eventId=event_id, sendNotifications=notify)

	def delete_events(self, event_id_list, notify=False):
		for eventt_id in event_id_list:
			self.delete_event(eventId=event_id, notify=true)
	
	def list_events(self):
		pageToken = None
		resp = self.__service.events().list(calendarId=self.__calendar_id, pageToken=pageToken).execute()
		for i in resp['items']:
			if 'end' in i and 'timeZone' in i['end'] and 'description' in i and 'htmlLink' in i:
				print '%s :::: %s :::: %s :::: %s :::: %s to %s' % (i['end']['timeZone'], i['description'], i['created'], i['htmlLink'], i['start']['dateTime'], i['end']['dateTime'])


	def update_event(self, event_id, event_body, notify=False):
		return self.__service.events().update(calendarId=self.__calendar_id, eventId=event_id, body=event_body.toJSON(), sendNotifications=notify).execute()


class EventBody:
	"""A class to describe a calendar event"""
	def __init__(self, summary, description, startTime, endTime, recurrances=None):
		obj = {
			'summary' : summary,
			'location' : '501 Shaw Ct, Severn, MD',
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
		"""For debugging: returns the internal representation of the EventBody"""
		print "OBJ: ",self.obj 
		return self.obj

	def toJSON(self):
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
