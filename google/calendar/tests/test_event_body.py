import unittest
from UASCalendar import EventBody

class TestEventBody(unittest.TestCase):
  def setUp(self):
    self.eb = EventBody(summary="test summary", description="test desc", startTime="2015-12-05 12:00:00-06:00", endTime="2015-12-05 12:01:00-06:00", recurrences="weekly")
  
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
    self.assertEquals(summary, "test summary")
    
    #teardown
    
  def test_get_description(self):
    #setup
    event = self.eb
    
    #exercise
    description = event.getDescription()
    
    #verify
    self.assertEquals(description, "test desc")

  def test_get_start_time(self):
    #setup
    event = self.eb

    #exercise
    start_time = event.getStartTime()

    #verify
    self.assertEquals(start_time, "2015-12-05T12:00:00-06:00")

  def test_get_end_time(self):
    #setup
    event = self.eb

    #exercise
    end_time = event.getEndTime()

    #verify
    self.assertEquals(end_time, "2015-12-05T12:01:00-06:00")

  def test_has_recurrences(self):
    #setup
    event = self.eb

    #exercise
    recurrence = event.hasrecurrences()

    #verify
    self.assertTrue(recurrence)

  def test_get_recurrences(self):
    #setup
    event = self.eb

    #exercise
    recurrence = event.getrecurrence()

    #verify
    self.assertEquals(recurrence, 'RRULE:FREQ=WEEKLY;')

  def test_raises_error_on_bad_recurrence(self):
    with self.assertRaises(ValueError):
      EventBody(summary="test summary", description="test desc", startTime="2015-12-05 12:00:00-06:00", endTime="2015-12-05 12:01:00-06:00", recurrences="wrong")

if __name__ == '__main__':
  unittest.main()
