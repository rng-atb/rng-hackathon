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
    
    def __init__(self):
        with open("lib/labels.json") as f:
            self.__CATEGORIES = json.loads(f.read())
        with open("lib/accounts.json") as f:
            self.__ACCOUNTSANDNAMES = json.loads(f.read())
        self.__POPULATE = populate()

    def getProfile(self):
        return self.__PROFILES

    def populateProfile(self):
        accounts = self.__ACCOUNTSANDNAMES.keys()
        
        for account in accounts:
            transactions = self.__POPULATE.getAllTransactionsByAccount(account = account)['transactions']
            name = self.__ACCOUNTSANDNAMES[account]
            for transaction in transactions:
                    if(transaction['details']['type'] == "FREE_FORM"):
                        merchant = transaction['details']['description']
                        label = self.getLabel(merchant)
                        if(label == None):
                            break
                        found = False
                        for jsonData in self.__PROFILES:
                            if(jsonData['source'] == name and jsonData['target'] == label):
                                jsonData['weight'] += 1
                                found = True
                                break
                        if(found == False):
                            jsonToAdd = {}
                            jsonToAdd['source'] = name
                            jsonToAdd['target'] = label
                            jsonToAdd['weight'] = 1
                            self.__PROFILES.append(jsonToAdd)

    def getLabel(self, merchant):
        labels = self.__CATEGORIES.keys()
        for label in labels:
            if(merchant in self.__CATEGORIES[label]):
                return label
            if(merchant == 'deposit'):
                return None
        raise Exception("Cant find label for merchant: " + merchant)


#profile = Profile()
#profile.populateProfile()
#print(profile.getProfile())

            
        
            
    
