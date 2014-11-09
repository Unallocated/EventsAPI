from httplib2 import Http
from oauth2client.client import SignedJwtAssertionCredentials
from apiclient.discovery import build

config = {}
execfile('gauth.cfg', config)

clientEmail = config['email']
keyFile = config['keyfile']

def read_key():
    with open(keyFile) as f:    
        privateKey = f.read()

    return privateKey

def authenticate(app, version, scope, sub=None):
    privateKey = read_key()

    if (not sub):
        credentials = SignedJwtAssertionCredentials(clientEmail, privateKey, scope)
    else:
        credentials = SignedJwtAssertionCredentials(clientEmail, privateKey, scope, sub)


    httpAuth = credentials.authorize(Http())
    service = build(app, version, http=httpAuth)
    return service
