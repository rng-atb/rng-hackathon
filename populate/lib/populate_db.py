"""
* You can use a decorator class to raise Exceptions on bad requests

*Get all accounts
*Get all transactions by accounts

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
		self.__ACCOUNT = account if account is not None and self.__ACCOUNT is None else None
		amount = random.randint(1, 20)
		url = self.__BASE__URL + "banks/" + self.__BANK__ID \
				+ "/accounts/{ACCOUNT_ID}/{VIEW_ID}/transaction-request-types/FREE_FORM/transaction-requests".format(ACCOUNT_ID=self.__ACCOUNT, VIEW_ID=self.__VIEW__ID)
		data = {"value":{"currency":"CAD","amount":amount},"description":description}
		r = requests.post(url, data=data,headers=self.__HEADER)
		print(data)
		print(url)
		print(r.status_code)
#		if (r.status_code is not 200):
#			raise Exception("Incorrect request!")
#		return r.text

	def getAllTransactionsByAccount(self, bank_id=None, account=None):
		self.__ACCOUNT = account if account is not None and self.ACCOUNTS is None else None

		self.__BANK__ID = bank_id if self.__BANK__ID is not None and bank_id is not None else None

		url = self.__BASE__URL + "banks/{BANK_ID}/accounts/{ACCOUNT_ID}/owner/transactions".format(BANK_ID=self.__BANK__ID, ACCOUNT_ID=self.__ACCOUNT)

		r = requests.get(url, headers=self.__HEADER)

		if (r.status_code is not 200):
			raise Exception("Incorrect request!")
		return r.text

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
		try:
			for account in self.account_data:
				for label in self.label_data:
					print(label)
					for merchant in label:
						self.populate_data.createTransaction(merchant, account)
		except Exception as e:
			print(e.args)
			#print('Error on line {}'.format(sys.exc_info()[-1].tb_lineno)
#Testing
#p = populate()
#print(p.getAllAccountsAtBank())
#print(p.getAllTransactionsByAccount())

c = create_data()
print(c.createTransactions())
