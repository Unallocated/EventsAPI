from authenticate import GoogleAuthentication

class UASCalendar:
	"""A class to interact with the Google Calendar API v3"""
	def __init__(self):
		"""Authenticates with google and selects the calendar to act on"""
		google = GoogleAuthentication("gauth.cfg")
		self.__service = google.authenticate(app="calendar", version='v3', scope='profile https://www.googleapis.com/auth/calendar')
		self.__calendar_id = self.__get_primary_calendar()['id']

	def list_calendars(self):
		"""Returns the list of calendars associated with the authenticated account"""
		calendars = []
		page_token = None
		while True:
			calendar_list = self.__service.calendarList().list(pageToken=page_token).execute()
			for calendar_list_entry in calendar_list['items']:
				calendars.append(calendar_list_entry)
				page_token = calendar_list.get('nextPageToken')
			if not page_token:
				break

		return calendars

	def __get_primary_calendar(self):
		"""Private: Returns the primary calendar in the account"""
		primary_calendar = None
		calendars = self.list_calendars()
		for calendar in calendars:
			try:
				calendar["primary"]
				primary_calendar=calendar
				break
			except KeyError:
				pass

		return primary_calendar

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
	def __init__(self, summary, description, startTime, endTime, location='501 Shaw Ct, Severn, MD', recurrences=None):
		allowed_recurrence = ["daily", "weekly", "monthly", "yearly"]
		if not recurrences in allowed_recurrence:
			raise ValueError("That is not an allowed value for recurrence")

		obj = {
			'summary' : summary,
			'location' : location,
			'description' : description,
			'start' : {
				'dateTime': startTime.replace(" ", "T")
			},
			'end' : {
				'dateTime': endTime.replace(" ", "T")
			},
			'recurrence' : 'RRULE:FREQ=' + recurrences.upper() + ';'
		}

		self.obj = obj

	def getSummary(self):
		return self.obj['summary']

	def getDescription(self):
		return self.obj['description']

	def getStartTime(self):
		return self.obj['start']['dateTime']

	def getEndTime(self):
		return self.obj['end']['dateTime']

	def getrecurrences(self):
		return self.obj['recurrences']

	def hasrecurrences(self):
		return not self.obj['recurrence'] == None

	def getrecurrence(self):
		return self.obj['recurrence']

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
