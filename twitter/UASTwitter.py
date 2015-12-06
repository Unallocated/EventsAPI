import sys
import os
import tweepy
from ConfigParser import ConfigParser
import logging
import base64
import tempfile
import cStringIO
import PIL.Image

class UASTwitter:
	"""
	This module connects to Twitter using credentials stored in the file name passed to the constructor.
	The only actions available are: 
	* post a text message
	* post a text message with an image file
	* post a text message with an image in base64 format
	"""

	# Path to the config file
	__configFilePath = ''
	# Handle to the config file (for getting configs)
	__configHandle = ConfigParser
	# Connection to Twitter
	__twitterHandle = None
	# Object that contains the Twitter authentication information
	__twitterAuthObject = None

	def __init__(self, configFilePath):
		""" Reads the configuration file, validates that all the required fields are present in the config
		file, creates the Twitter authentication object, and finally, connects and verifies the connection to 
		Twitter

		Raises Exception if:
			The configFilePath is empty
			The Config file is missing
			One or more config entries are missing
			The connection to Twitter fails

		The configuration file is expected to be in the following format:
			[consumer]
			key = SOMEKEY
			secret = MYSECRET

			[access]
			key = ANOTHERKEY
			secret = ANOTHERSECRET

		"""

		if len(configFilePath) == 0:
			raise Exception("The config file path was empty")

		self.__configFilePath = configFilePath
		self.__validateConfigFile()

		self.__twitterAuthObject = tweepy.OAuthHandler(self.getConsumerKey(), self.getConsumerSecret())
		self.__twitterAuthObject.set_access_token(self.getAccessKey(), self.getAccessSecret())
		
		self.__twitterHandle = tweepy.API(self.__twitterAuthObject)

		try:
			self.__twitterHandle.me()
		except tweepy.error.TweepError as e:
			raise Exception("Could not get user information.  This likely means that the connection could not be established, or that the authentication information is not correct.  Details: %s" % e.message)

	def postWithImage(self, message, fileName):
		""" Posts a status to Twitter along with a single image.

		message must be a string
		fileName must be a string path to a file that contains a single image

		The file will be checked to ensure that it is, indeed, an image

		Raises Exception if:
			The message is empty
			The file provided does not exist
			The file provided does not contain an image
			The post to Twitter fails

		"""
		
		if len(message) == 0:
			raise Exception("Message contained no characters")

		if os.path.isfile(fileName) == False:
			raise Exception("File '%s' does not exist" % (fileName))
			
		if self.__fileIsImage(fileName) == False:
			raise Exception('File was not a valid image!!!')

		self.__twitterHandle.update_with_media(fileName, message)
	
	def __fileIsImage(self, fileName):
		""" Checks to make sure that a file contains a valid image.  Uses PIL.Image to verify the file contains an image

		fileName must be a string that points to a file

		Raises Exception if:
			The file does not exist
		
		Returns:
			True if the file is an image
			False if the file is not an image

		"""
		if os.path.isfile(fileName) == False:
			raise Exception("File '%s' does not exist" % (fileName))

		try:
			PIL.Image.open(fileName)
		except IOError as e:
			return False

		return True
	
	def postWithImageBase64(self, message, base64Image):
		""" Posts an image to Twitter with an attached image.  

		message must be a string
		base64Image must be a base64 encoded string

		Raises Exception if:
			message is an empty string
			base64Image is an empty string
			The base64image, when decoded, is not an image
			The temp file could not be cleaned up
			Posting to Twitter fails

		"""
		if len(message) == 0:
			raise Exception("No message was provided")

		if len(base64Image) == 0:
			raise Exception("No base64 data was passed in")

		# The extention here is only to make the Twitter library happy
		tempFile = tempfile.NamedTemporaryFile(delete=False, suffix=".jpg")
		tempFile.write(base64.b64decode(base64Image))
		tempFile.close()

		try:
			if self.__fileIsImage(tempFile.name) == False:
				raise Exception('File was not an image!!!')

			self.__twitterHandle.update_with_media(tempFile.name, message)
		except Exception as e:
			# re-throw the exception
			raise e
		finally:
		  # cleanup the temp file
			os.unlink(tempFile.name)

			if os.path.exists(tempFile.name):
				raise Exception("Could not remove temp file '%s'" % tempFile.name)

	def post(self, message):
		""" Posts a message to Twitter

			message must be a string

			Raises Exception if:
				message is an empty string
				The post to Twitter fails

		"""
		
		if len(message) == 0:
			raise Exception("No message was provided")

		self.__twitterHandle.update_status(message)

	def getAccessKey(self):
		""" Getter for the Twitter access key """
		return self.__configHandle.get('access', 'key')
	
	def getAccessSecret(self):
		""" Getter for the Twitter access secret """
		return self.__configHandle.get('access', 'secret')
	
	def getConsumerKey(self):
		""" Getter for the Twitter consumer key """
		return self.__configHandle.get('consumer', 'key')
	
	def getConsumerSecret(self):
		""" Getter for the Twitter consumer secret """
		return self.__configHandle.get('consumer', 'secret')
	
	def __validateConfigFile(self):
		""" Makes sure that the config file contains all of the required information 
		
			Raises Exception if:
				Any field is not present

		"""
		if os.path.isfile(self.__configFilePath) == False:
			raise Exception("The configuration file '%s' does not exist" % (self.__configFilePath))
		self.__configHandle = ConfigParser()
		self.__configHandle.read(self.__configFilePath)

		try:
			self.getConsumerKey()
		except:
			raise Exception("Could not find consumer key in config file '%s'", self.__configFilePath)

		try:
			self.getConsumerSecret()
		except:
			raise Exception("Could not find consumer secret in config file '%s'", self.__configFilePath)

		try:
			self.getAccessKey()
		except:
			raise Exception("Could not find access key in config file '%s'", self.__configFilePath)

		try:
			self.getAccessSecret()
		except:
			raise Exception("Could not find access secret in config file '%s'", self.__configFilePath)

