"""
* You can use a decorator class to raise Exceptions on bad requests

*Get all accounts
*Get all transactions by accounts

"""
import json
import requests

class populate:
	__BASE__URL = "https://api.leapos.ca/obp/v4.0.0/"
	__TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyIiOiIifQ.i6uCFJJKYmjJvj6S3XoSGvxPB1TsxtbJyCPxgtB6ZFI"
	__USER__ID = "b4b397f4-ca49-4284-99a4-2654ef82f597"

	__BANK__ID = "bda5596ed24e2c440db4ade11f65d34"
	__BRANCH__ID = "271994d2-2c85-4dbe-9fb6-6cf22df7cfba"
	__ACCOUNTS = ["account_1","account_2","account_3"]

	__HEADER = {}
	__VIEW__ID = "owner"

	def __init__(self, token=None, user_id=None, bank_id=None):
		self.__HEADER['Authorization'] = 'DirectLogin token=\"eyJhbGciOiJIUzI1NiJ9.eyIiOiIifQ.i6uCFJJKYmjJvj6S3XoSGvxPB1TsxtbJyCPxgtB6ZFI\"'

	def getCurrentUser(self):
		url = self.__BASE__URL + "users/current"
		r = requests.get(url, headers=self.__HEADER.format(TOKEN=self.__TOKEN))
		if (r.status_code is not 200):
			raise Exception("Incorrect request")
		return r.text

	def getAllAccountsAtBank(self, bank_id=None):
		url = self.__BASE__URL + "banks/" + self.__BANK__ID + "/accounts"
		r = requests.get(url, headers=self.__HEADER)
		if (r.status_code is not 200):
			raise Exception("Incorrect request!")
		return r.text

	def getCustomersAtBank(self, bank_id=None):
		url = self.__BASE__URL + "customers"
		r = requests.get(url, headers=self.__HEADER.format(TOKEN=self.__TOKEN))
		if (r.status_code is not 200):
			raise Exception("Incorrect request!")
		return r.text

	def getAccountViews(self, bank_id=None, account_id=None):
		url = self.__BASE__URL + "banks/" + self.__BANK__ID + "/accounts/" + self.__ACCOUNT__ID + "/views"
		r = requests.get(url, headers=self.__HEADER.format(TOKEN=self.__TOKEN))
		if (r.status_code is not 200):
			raise Exception("Incorrect request!")
		return r.text

	def createTransaction(self, description=None):
		url = self.__BASE__URL + "banks/" + self.__BANK__ID \
				+ "/accounts/{ACCOUNT_ID}/{VIEW_ID}/transaction-request-types/FREE_FORM/transaction-requests".format(ACCOUNT_ID=self.__ACCOUNT__ID, VIEW_ID=self.__VIEW__ID)
		data = {"value":{"currency":"CAD","amount":"10"},"description":"This is a FREE_FORM Transaction Request"}
		r = requests.post(url, data=json.dumps(data),headers=self.__HEADER.format(TOKEN=self.__TOKEN))

		if (r.status_code is not 200):
			raise Exception("Incorrect request!")

		return r.text

	def getAllTransactionsByAccount(self, bank_id=None):
		for account in range(0, len(self.__ACCOUNTS)):
			url = self.__BASE__URL + "banks/{BANK_ID}/accounts/{ACCOUNT_ID}/owner/transactions".format(BANK_ID=self.__BANK__ID, ACCOUNT_ID=self.__ACCOUNTS[account])
			print(url)
			r = requests.get(url, headers=self.__HEADER)

			if (r.status_code is not 200):
				raise Exception("Incorrect request!")
			return r.text

#Testing
#p = populate()
#print(p.getAllAccountsAtBank())
#print(p.getAllTransactionsByAccount())
