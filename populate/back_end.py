import json

class Profile:
    __CATEGORIES = None
    __PROFILES = []
    __POPULATE = None
    
    def __init__(self, jsonFile):
        with open(jsonFile) as f:
            self.__CATEGORIES = json.loads(f)
        self.__POPULATE = populate()
        accounts = self.__POPULATE.getAllAccountsAtBank()
        for account in accounts:
            if(account['id'].Contains("account_")):
                self.__PROFILES[account['id']] = None

    def populateProfiles():
        
            
    
