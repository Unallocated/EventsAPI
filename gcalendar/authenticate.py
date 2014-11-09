from httplib2 import Http
from oauth2client.client import SignedJwtAssertionCredentials
from apiclient.discovery import build

def authenticate():
    """
    authenticate with google calendar. Uses OAuth2.0
    """

    client_email = '475940943373-57fj7haui59r6t5iir1p19r9q0kf3qho@developer.gserviceaccount.com'
    with open("./key/eventsapikey.pem") as f:    
        private_key = f.read()

        credentials = SignedJwtAssertionCredentials(client_email, private_key,
                'https://www.googleapis.com/auth/calendar')

    http_auth = credentials.authorize(Http())
    service = build('calendar', 'v3', http=http_auth)
    return service
