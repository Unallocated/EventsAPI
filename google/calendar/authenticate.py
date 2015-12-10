import httplib2
from oauth2client import client
from oauth2client.file import Storage
from apiclient import discovery
import webbrowser
import httplib2

class GoogleAuthentication:
	"""A wrapper around the Google Authentication library"""
	def __init__(self, configLocation):
		"""Read the configuration file and make the variables available as class variables"""
		config = {}
		execfile(configLocation, config)

		self.clientEmail = config['email']
		self.keyFile = config['keyFile']
		self.keyPass = config['keyPassword']

	def authenticate(self, app, version, scope, sub=None):
		"""Perform OAuth2 with Google to get an access token"""
		storage = Storage('.credential_file') 
		flow = client.flow_from_clientsecrets('client_secrets.json', scope="profile https://www.googleapis.com/auth/calendar", redirect_uri='urn:ietf:wg:oauth:2.0:oob')
		
		if storage.get():
			credentials = storage.get()
		else:
			auth_uri = flow.step1_get_authorize_url()
			webbrowser.open(auth_uri)
			auth_code = raw_input('Enter the auth code: ')
			credentials = flow.step2_exchange(auth_code)
			storage.put(credentials)

		http_auth = credentials.authorize(httplib2.Http())
		service = discovery.build(serviceName=app, version=version, http=http_auth)
		return service

