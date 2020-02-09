import json
import csv
import sys
import os
import pandas
sys.path.insert(1,'lib/')
# from populate_db import populate
# from make_html import createTable
# from make_html import closeHTML
# from make_html import beginHTML
from .lib.populate_db import populate
from .make_html import createTable
from .make_html import closeHTML
from .make_html import beginHTML


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

    def writeToFile(self, filename):
        with open(filename, 'w', newline='') as f:
            f.write(str(self.__PROFILES))
            f.close()

    def getInterestedProfiles(self, target, weight):
        profile = self.getProfile()
        filteredList = []
        for item in profile:
            if (item['target'] == target and int(item['weight']) >= weight):
                filteredList.append(item)
        return filteredList

    def createReportHtml(self, interest, weight):
        if(os.path.exists("index.html")):
            os.remove("index.html")
        profiles = self.getInterestedProfiles(interest, weight)
        profiles.sort(key = lambda x:x['weight'], reverse = True)
        print(profiles)
        beginHTML()
        for profile in profiles:
            createTable(profile['source'], profile['target'], profile['weight'])

        closeHTML()

    def writeToCsv(self, filename):
        if(os.path.exists(filename)):
            os.remove(filename)
        profiles = self.getProfile()
        srcCol = [profile['source'] for profile in profiles]
        targetCol = [profile['target'] for profile in profiles]
        weightCol = [profile['weight'] for profile in profiles]
        df = pandas.DataFrame(data={"source": srcCol, "target": targetCol, "weight": weightCol})
        df.to_csv(filename, sep=',',index=False)

if __name__ == "__main__":
    interest = sys.argv[1]
    weight = sys.argv[2]
      
    profile = Profile()
    profile.populateProfile()
    profile.createReportHtml(interest, weight)
    #profile.writeToCsv("data.csv")
    #profile.createReportHtml()
    #profile.writeToFile("profiles.json")
    #print(profile.getInterestedProfiles("Learning", 7))
