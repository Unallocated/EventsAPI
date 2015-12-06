import unittest
from UASCalendar import EventBody

class TestEventBody(unittest.TestCase):
  def test_create_event(self):
    #setup
    #exercise
    eb = EventBody("test summary", "test desc", "2015-12-05T12:00:00-06:00", "2015-12-05T12:01:00-06:00")
    
    #verify
    self.assertIsInstance(eb, EventBody)

    #teardown

  def test_get_summary(self):
    pass
    #setup
    #exercise
    #verify
    #teardown

if __name__ == '__main__':
  unittest.main()
