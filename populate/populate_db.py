"""
* You can use a decorator class to raise Exceptions on bad requests

"""
import json
import requests
import pymysql

class populate:
	__BASE__URL = "https://api.leapos.ca/obp/v4.0.0/"
	__TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyIiOiIifQ.i6uCFJJKYmjJvj6S3XoSGvxPB1TsxtbJyCPxgtB6ZFI"
	__USER__ID = "b4b397f4-ca49-4284-99a4-2654ef82f597"

	__BANK__ID = "bda5596ed24e2c440db4ade11f65d34"
	__BRANCH__ID = "271994d2-2c85-4dbe-9fb6-6cf22df7cfba"
	__ACCOUNT__ID = ["account_1","account_2","account_3"]
	__HEADER = {"Authorization": "DirectLogin token=\"{TOKEN}\""}


	__SESSION = None

	def __init__(self, token, user_id, bank_id):
		self.__TOKEN = token
		self.__USER__ID = user_id
		self.__BANK__ID = bank_id

	def getCurrentUser(self):
		url = self.__BASE__URL + "users/current"
		r = requests.get(url, json=self.__HEADER.format(TOKEN=self.__TOKEN))
		if (r.status_code is not 200):
			raise Exception("Incorrect request")
		return r.text

	def getAllAccountsAtBank(self, bank_id=None):
		url = self.__BASE__URL + "banks/" + self.__BANK__ID + "/accounts"
		r = requests.get(url, json=self.__HEADER.format(TOKEN=self.__TOKEN))
		if (r.status_code is not 200):
			raise Exception("Incorrect request!")
		return r.text

	def getCustomersAtBank(self, bank_id=None):
		url = self.__BASE__URL + "customers"
		r = requests.get(url, json=self.__HEADER.format(TOKEN=self.__TOKEN))
		if (r.status_code is not 200):
			raise Exception("Incorrect request!")
		return r.text

	def getAccountViews(self, bank_id=None, account_id=None):
		url = self.__BASE__URL + "banks/" + self.__BANK__ID + "/accounts/" + self.__ACCOUNT__ID + "/views"
		r = requests.get(url, json=self.__HEADER.format(TOKEN=self.__TOKEN))
		if (r.status_code is not 200):
			raise Exception("Incorrect request!")
		return r.text 
	def createAccount(self):
		pass

	def createTransactionType(self):
		r = requests.post(self.__BASE_URL, auth=('user', 'pass'))

	def createTransaction(self, metadata=None):
		pass

	def createAccount(self):
		pass

	def getTransactionTypes(self):
		pass

	def getBranches(self):
		pass

	def getBankProducts(self):
		pass

	def getAllAvailableRoles(self):
		pass

class randomize:
	def __init__(self):
		pass

	def getFName(self):
		pass

	def getLName(self):
		pass

	def getAddress(self):
		pass


class businesses:
	def __init__(self):
		pass

	def insertBusinessIntoDB(self):
		pass
