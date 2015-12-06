import unittest
from UASCalendar import EventBody

class TestEventBody(unittest.TestCase):
  def setUp(self):
    self.eb = EventBody("test summary", "test desc", "2015-12-05T12:00:00-06:00", "2015-12-05T12:01:00-06:00")
  
  def test_create_event(self):
    #exercise
    event = self.eb
    
    #verify
    self.assertIsInstance(event, EventBody)
    
  def test_get_summary(self):
    #setup
    event = self.eb
    
    #exercise
    summary = event.getSummary()
    
    #verify
    self.assertEqual(summary, "test summary")
    
    #teardown
    
  def test_get_description(self):
    #setup
    event = self.eb
    
    #exercise
    description = event.getDescription()
    
    #verify
    self.assertEquals(description, "test desc")
    

if __name__ == '__main__':
  unittest.main()
