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
		"""Takes an `EventBody` object and posts it to the calendar

		Returns the event object from Google which includes a link to the event
		"""
		return self.__service.events().insert(calendarId=self.__calendar_id, body=event_body.toJSON()).execute()

	def delete_event(self, event_id, notify=True):
		"""Takes an event_id and deletes it"""
		self.__service.events().delete(calendarId=self.__calendar_id, eventId=event_id, sendNotifications=notify)

	def delete_events(self, event_id_list, notify=True):
		"""The same as `delete_event` except for multiple events"""
		for event_id in event_id_list:
			self.delete_event(eventId=event_id, notify=notify)
	
	def list_events(self):
		"""This lists all of the events in the calendar.  Be warned, this can be a lot!"""
		pageToken = None
		resp = self.__service.events().list(calendarId=self.__calendar_id, pageToken=pageToken).execute()
		return resp['items']

	def update_event(self, event_id, event_body, notify=True):
		"""Takes an event_id and a new `EventBody` and updates the event_id to the new event details"""
		return self.__service.events().update(calendarId=self.__calendar_id, eventId=event_id, body=event_body.toJSON(), sendNotifications=notify).execute()


class EventBody:
	"""A class to describe a Google calendar event"""
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