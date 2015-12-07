import httplib2
from oauth2client import client
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
		self.keyFile = config['keyfile']
		self.keyPass = config['keypass']
		self.privateKey = self.read_key(self.keyFile)

	def read_key(self, keyfile):
		"""Read the private key"""
		with open(keyfile) as f:    
			privateKey = f.read()

		return privateKey

	def authenticate(self, app, version, scope, sub=None):
		"""Perform OAuth2 with Google to get an access token"""
		# client_secrets.json was given from google to the application on the auth panel,
		# 	it contains the OAuth secret and key
		#
		# This redirect URI means to open a window with the code and tell the user to paste it into the app
		flow = client.flow_from_clientsecrets('client_secrets.json', scope="profile https://www.googleapis.com/auth/calendar", redirect_uri='urn:ietf:wg:oauth:2.0:oob')
		auth_uri = flow.step1_get_authorize_url()
		webbrowser.open(auth_uri)
		auth_code = raw_input('Enter the auth code: ')
		credentials = flow.step2_exchange(auth_code)
		http_auth = credentials.authorize(httplib2.Http())
		service = discovery.build(serviceName=app, version=version, http=http_auth)
		print service
		return service

