from UASTwitter import UASTwitter
import uuid
import base64

a = UASTwitter('twitter.conf')
a.post('this is a test %s' % (uuid.uuid4()))
a.postWithImage('hi from bill %s' % (uuid.uuid4()), '/home/main/Downloads/bill.jpg')

with open("/home/main/Downloads/bill.jpg", "rb") as imageFile:
	b64 = base64.b64encode(imageFile.read())	
a.postWithImageBase64('hi from bill %s' % (uuid.uuid4()), b64) 

try:
	a.postWithImage('what what in the butt', 'twitter.py')
except:
	print 'yay!'

