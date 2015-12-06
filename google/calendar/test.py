import unittest
from UASCalendar import EventBody, UASCalendar
import json

class TestEventBody(unittest.TestCase):
  def test_create_event(self):
    #setup
    eb = EventBody("test summary", "test desc", "2015-12-05T12:00:00-06:00", "2015-12-05T12:01:00-06:00")

    #exercise
    summary = eb.getSummary()

    #verify
    #teardown

if __name__ == '__main__':
  unittest.main()

#uc = UASCalendar()
#gcal_event = uc.create_event(eb)
#print gcal_event['id']
#devnt = uc.delete_event(gcal_event['id'])
#print devnt

