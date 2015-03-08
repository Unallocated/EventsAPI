from flask import Flask
from flask import request
import logging
import json
import sys
import uuid

sys.path.append('../twitter')
from UASTwitter import UASTwitter
twitter = UASTwitter('../twitter/twitter.conf')

#sys.path.append('../google/calendar/')
from UASCalendar import UASCalendar, EventBody

calendar = UASCalendar()

app = Flask(__name__)

class ParsedEvent:
	def __init__(self, event):
		self.startDate = event['value']
		self.endDate = event['value2']
		self.rule = event['rrule']
	
	def getStartDate(self):
		return self.startDate
	
	def getEndDate(self):
		return self.endDate
	
	def getRule(self):
		return self.rule


class ParsedRequest:
	
	def __init__(self, jsonRequest):
		
		if not 'uuid' in jsonRequest.keys():
			raise Exception("No UUID field present!")

		if not 'body' in jsonRequest:
			raise Exception("No body field present!")

		if not 'und' in jsonRequest['body']:
			raise Exception("No und field present!")

		if len(jsonRequest['body']['und']) == 0:
			raise Exception("There are no elements in the body")

		if not 'safe_value' in jsonRequest['body']['und'][0]:
			raise Exception("No title found")

		self.uuid = jsonRequest['uuid']
		self.title = jsonRequest['body']['und'][0]['safe_value']
		self.summary = jsonRequest['body']['und'][0]['safe_summary']
		self.events = []
		
		for i in jsonRequest['field_event_date']['und']:
			self.events.append(ParsedEvent(i))


	def getEvents(self):
		return self.events

	def getUUID(self):
		return self.uuid
	
	def getTitle(self):
		return self.title
	
	def getSummary(self):
		return self.summary

@app.route("/events/create", methods = ["POST"])
def createEvent():
	try:
		a = ParsedRequest(request.json)
	except Exception as e:
		print "Exception: %s" % e
		return "Could not process request.  Details: %s" % (e)
	
	try:
		twitter.post("%s%s" % (uuid.uuid1(), a.getSummary()))
	except Exception as e:
		print "Twitter exception: %s" % e
		return "Could not post to Twitter"
	try:
		calendar.create_event({
			'summary' : 'Thisasdfsdfsdfsdf is a test',
			'location' : '501 Shaw dsfsdfsdfsdfCt',
			'start' : { 
				'dateTime' : '2015-04-10T08:00:00.000-06:00'
			},  
			'end' : { 
				'dateTime' : '2015-04-10T09:00:00.000-06:00'
			}   
		})
	except Exception as e:
		print "Exception: %s" % e
		return "ACK"

	return "id"

if __name__ == "__main__":
	app.run()
