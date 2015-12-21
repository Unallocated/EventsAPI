import unittest
from mockGoogleCalendar import mockGoogleCalendar
from UASCalendar import EventBody, UASCalendar
import json

class TestUASCalendar(unittest.TestCase):
  def setUp(self):
    self.event = EventBody(summary="test summary", description="test desc", startTime="2015-12-05 12:00:00-06:00", endTime="2015-12-05 12:01:00-06:00", recurrences="weekly")
    self.calendar = UASCalendar()
    self.calendar._UASCalendar__service = mockGoogleCalendar()

  def test_create_calendar_object(self):
    self.assertIsInstance(self.calendar,UASCalendar)

  def test_list_calendars(self):
    #setup
    calendar = self.calendar

    #exercise
    summaries = []
    calendars = calendar.list_calendars()
    for calendar in calendars:
      summaries.append(calendar["summary"])

    #verify
    self.assertEquals(['Moo', 'Test Events Calendar', 'uas.events.tester@gmail.com'], summaries)

  def test_primary_calendar(self):
    #setup
    calendar = self.calendar

    #exercise
    primary_calendar = calendar._UASCalendar__get_primary_calendar()

    #verify
    self.assertEquals(primary_calendar["summary"], 'uas.events.tester@gmail.com')


if __name__ == '__main__':
  unittest.main()