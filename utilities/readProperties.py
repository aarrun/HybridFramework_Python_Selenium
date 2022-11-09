import configparser

config = configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")


class ReadConfig:
	@staticmethod
	def getApplicationURL():
		URL = config.get("common info", "baseURL")
		return URL

	@staticmethod
	def getUserEmail():
		Email = config.get("common info", "email")
		return Email

	@staticmethod
	def getPassword():
		Password = config.get("common info", "password")
		return Password
