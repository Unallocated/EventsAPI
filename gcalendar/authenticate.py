from httplib2 import Http
from oauth2client.client import SignedJwtAssertionCredentials
from apiclient.discovery import build

config = {}
execfile('gauth.cfg', config)

clientEmail = config['email']
keyFile = config['keyfile']
scope = config['scope']

print "{} {} {}".format(clientEmail, keyFile, scope)

def authenticate():
    """
    authenticate with google calendar. Uses OAuth2.0
    """

    with open(keyFile) as f:    
        privateKey = f.read()
        credentials = SignedJwtAssertionCredentials(clientEmail, privateKey, scope)

    httpAuth = credentials.authorize(Http())
    service = build('calendar', 'v3', http=httpAuth)
    return service
