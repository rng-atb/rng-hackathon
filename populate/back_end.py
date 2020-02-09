import json
import sys
sys.path.insert(1,'lib/')
from populate_db import populate


class Profile:
    __CATEGORIES = None
    __ACCOUNTSANDNAMES = None
    __PROFILES = []
    __ACCOUNTLIST = []
    __POPULATE = None
    __ACCOUNTTONAME = []
    
    def __init__(self, jsonFile):
        with open("lib/labels.json") as f:
            self.__CATEGORIES = json.loads(f.read())
        with open("libs/accounts.json") as f:
            self.__ACCOUNTSANDNAMES = json.loads(f.read())
            
        self.__POPULATE = populate()

    def getProfile(self):
        return self.__PROFILES

    def populateProfile(self):
        accounts = self.__ACCOUNTSANDNAMES.keys()
        
        for account in accounts:
            transactions = self.__POPULATE.getAllTransactionsByAccount(account)
            name = self.__ACCOUNTSANDNAMES[account]
            
            for transaction in transactions:
                if(transaction['details']['type'] == "FREE_FORM"):
                    merchant = transaction['details']['description']
                    label = self.getLabel(merchant)
                    found = False
                    for (jsonData in self.__PROFILES):
                        if(jsonData['source'] = name and jsonData['target'] = label):
                            jsonData['weight'] += 1
                            found = True
                            break
                    if(found = False):
                        jsonToAdd['source'] = name
                        jsonToAdd['target'] = label
                        jsonToAdd['weight'] = 1
                        self.__PROFILES.append(jsonToAdd)
'''
format:
[
  {
    "source": "Account1",
    "target": "Learning",
    "value": 10
  },
  {
    "source": "Account1",
    "target": "Outdoors",
    "value": 20
  },
  {
    "source": "Account2",
    "target": "Gaming",
    "value": 10
  },
  {
    "source": "Account3",
    "target": "Learning",
    "value": 10
  }
]
'''
                            

    def getMerchant(self, merchant):
        labels = self.__CATEGORIES.keys()
        for label in labels:
            if(self.__CATEGORIES[label].contains(merchant)):
                return label
        raise Exception("Cant find label for merchant: " + merchant)


profile = Profile()
profile.populateProfile()
print(profile.getProfile())

            
        
            
    
