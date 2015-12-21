class mockGoogleCalendar:
  def __init__(self):
    self.mockResponse = None
    self.calendars = {
    "items":
      [
        {u'kind': u'calendar#calendarListEntry', u'foregroundColor': u'#000000', u'defaultReminders': [], u'colorId': u'22', u'selected': True, u'summary': u'Moo', u'etag': u'"1449366918343000"', u'backgroundColor': u'#f691b2', u'timeZone': u'America/New_York', u'accessRole': u'owner', u'id': u'r2ekf1cbgo3n8hilm9pbopvbhg@group.calendar.google.com'},
        {u'kind': u'calendar#calendarListEntry', u'foregroundColor': u'#000000', u'defaultReminders': [], u'description': u'This Calendar is to test the Events API', u'colorId': u'11', u'selected': True, u'summary': u'Test Events Calendar', u'etag': u'"1449366039162000"', u'location': u'Maryland', u'backgroundColor': u'#fbe983', u'timeZone': u'America/New_York', u'accessRole': u'owner', u'id': u'p5u176mnpog3kv4mrtgaq42618@group.calendar.google.com'},
        {u'kind': u'calendar#calendarListEntry', u'foregroundColor': u'#000000', u'defaultReminders': [{u'minutes': 30, u'method': u'popup'}], u'primary': True, u'colorId': u'17', u'selected': True, u'notificationSettings': {u'notifications': [{u'type': u'eventCreation', u'method': u'email'}, {u'type': u'eventChange', u'method': u'email'}, {u'type': u'eventCancellation', u'method': u'email'}, {u'type': u'eventResponse', u'method': u'email'}]}, u'summary': u'uas.events.tester@gmail.com', u'etag': u'"1449366919668000"', u'backgroundColor': u'#9a9cff', u'timeZone': u'America/New_York', u'accessRole': u'owner', u'id': u'uas.events.tester@gmail.com'}
      ]
    }

    self.events = [
      {u'status': u'confirmed', u'kind': u'calendar#event', u'end': {u'dateTime': u'2011-06-03T13:25:00-04:00'}, u'created': u'2014-11-08T23:25:50.000Z', u'iCalUID': u'tkvn9nndf20riojo99rk17elns@google.com', u'reminders': {u'useDefault': True}, u'htmlLink': u'https://calendar.google.com/calendar/event?eid=dGt2bjlubmRmMjByaW9qbzk5cmsxN2VsbnMgdWFzLmV2ZW50cy50ZXN0ZXJAbQ', u'sequence': 0, u'updated': u'2014-11-08T23:25:51.291Z', u'summary': u'Appointment', u'start': {u'dateTime': u'2011-06-03T13:00:00-04:00'}, u'etag': u'"2830978302582000"', u'location': u'Somewhere', u'attendees': [{u'self': True, u'displayName': u'Events Tester', u'email': u'uas.events.tester@gmail.com', u'responseStatus': u'needsAction'}], u'organizer': {u'displayName': u'bryan peace', u'email': u'0x9090cd80@gmail.com'}, u'creator': {u'displayName': u'bryan peace', u'email': u'0x9090cd80@gmail.com'}, u'id': u'tkvn9nndf20riojo99rk17elns'},
      {u'status': u'confirmed', u'kind': u'calendar#event', u'end': {u'dateTime': u'2014-11-09T12:25:00-05:00'}, u'created': u'2014-11-08T23:29:38.000Z', u'iCalUID': u'dlu1ermgve3gkre48pinqls324@google.com', u'reminders': {u'useDefault': True}, u'htmlLink': u'https://calendar.google.com/calendar/event?eid=ZGx1MWVybWd2ZTNna3JlNDhwaW5xbHMzMjQgdWFzLmV2ZW50cy50ZXN0ZXJAbQ', u'sequence': 0, u'updated': u'2014-11-08T23:29:39.089Z', u'summary': u'Appointment', u'start': {u'dateTime': u'2014-11-09T12:00:00-05:00'}, u'etag': u'"2830978758178000"', u'location': u'Somewhere', u'attendees': [{u'self': True, u'displayName': u'Events Tester', u'email': u'uas.events.tester@gmail.com', u'responseStatus': u'needsAction'}], u'organizer': {u'displayName': u'bryan p', u'email': u'0x9090cd80@gmail.com'}, u'creator': {u'displayName': u'bryan p', u'email': u'0x9090cd80@gmail.com'}, u'id': u'dlu1ermgve3gkre48pinqls324'}
    ]

  def calendarList(self):
    self.mockResponse = self.calendars
    return self

  def list(self,pageToken):
    return self

  def events(self):
    return self

  def execute(self):
    return self.mockResponse