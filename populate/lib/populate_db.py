"""
* You can use a decorator class to raise Exceptions on bad requests

*Get all accounts [done]
*Get all transactions by accounts [done]

p = populate()
print(p.getAllAccountsAtBank())
print(p.getAllTransactionsByAccount())

c = create_data()
print(c.createTransactions())

"""
import json
import requests
import random

class populate:
	__BASE__URL = "https://api.leapos.ca/obp/v4.0.0/"
	__TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyIiOiIifQ.i6uCFJJKYmjJvj6S3XoSGvxPB1TsxtbJyCPxgtB6ZFI"
	__USER__ID = "b4b397f4-ca49-4284-99a4-2654ef82f597"

	__BANK__ID = "bda5596ed24e2c440db4ade11f65d34"
	__BRANCH__ID = "271994d2-2c85-4dbe-9fb6-6cf22df7cfba"
	__ACCOUNT = ""

	__HEADER = {}
	__VIEW__ID = "owner"

	def __init__(self, token=None, user_id=None, bank_id=None, account=None):
		self.__HEADER['Authorization'] = 'DirectLogin token=\"eyJhbGciOiJIUzI1NiJ9.eyIiOiIifQ.i6uCFJJKYmjJvj6S3XoSGvxPB1TsxtbJyCPxgtB6ZFI\"'
		self.__HEADER['Content-Type'] = 'application/json'

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

	def getAccountViews(self, bank_id=None, account=None):
		self.__ACCOUNT = account if account is not None and self.__ACCOUNT is None else None
		url = self.__BASE__URL + "banks/" + self.__BANK__ID + "/accounts/" + self.__ACCOUNT + "/views"
		r = requests.get(url, headers=self.__HEADER.format(TOKEN=self.__TOKEN))
		if (r.status_code is not 200):
			raise Exception("Incorrect request!")
		return r.text

	def createTransaction(self, description=None, account=None):
		self.__ACCOUNT = account if self.__ACCOUNT is not None else account
		amount = random.randint(1, 20)
		url = self.__BASE__URL + "banks/" + self.__BANK__ID \
				+ "/accounts/{ACCOUNT_ID}/{VIEW_ID}/transaction-request-types/FREE_FORM/transaction-requests".format(ACCOUNT_ID=self.__ACCOUNT, VIEW_ID=self.__VIEW__ID)
		body = {}
		body["value"]={}
		body["value"]["currency"]="CAD"
		body["value"]["amount"]=str(amount)
		body["description"]=description
		r = requests.post(url, json=body,headers=self.__HEADER)
		if (r.status_code is not 201):
			error = "Incorrect request! ({status_code})"
			raise Exception(error.format(status_code=r.status_code))
		return r.text

	def getAllTransactionsByAccount(self, bank_id=None, account=None):
		self.__ACCOUNT = account
		url = self.__BASE__URL + "banks/{BANK_ID}/accounts/{ACCOUNT_ID}/owner/transactions".format(BANK_ID=self.__BANK__ID, ACCOUNT_ID=self.__ACCOUNT)
		r = requests.get(url, headers=self.__HEADER)
		if (r.status_code is not 200):
			raise Exception("Incorrect request!" + str(r.status_code))
		return json.dumps(r.text)

class create_data:
	label_location = "labels.json"
	label_data = None

	account_location = "accounts.json"
	account_data = None

	populate_data = populate()

	def __init__(self):
		with open(self.label_location, 'r') as f:
    			self.label_data = json.loads(f.read())

		with open(self.account_location, 'r') as f:
			self.account_data = json.loads(f.read())

	def createTransactions(self):
		labels = self.label_data.keys()
		accounts = self.account_data.keys()
		for account in accounts:
			for label in labels:
				merchants = self.label_data[label]
				for merchant in merchants:
					num = random.randint(0,3)
					if (num is not 0):
						self.populate_data.createTransaction(merchant, account)

