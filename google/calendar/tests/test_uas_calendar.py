import unittest
from UASCalendar import EventBody, UASCalendar
import json

class TestUASCalendar(unittest.TestCase):
  def test_create_calendar_object(self):
    #setup
    #None needed
    
    #exercise
    uc = UASCalendar()
    
    #verify
    self.assertIsInstance(uc,UASCalendar)
    
    #teardown

if __name__ == '__main__':
  unittest.main()
#uc = UASCalendar()
#gcal_event = uc.create_event(eb)
#print gcal_event['id']
#devnt = uc.delete_event(gcal_event['id'])
#print devnt
