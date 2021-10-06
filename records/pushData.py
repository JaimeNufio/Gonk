import json
import firestore

#!!!
def pushNicknames():
    with open('names.json') as f:
        data = json.loads(f.read())
        
        db = None

        firestore.init("../firebase.json")

        for user in data.keys():
            print(user)

            for obj in data[user]:

                documentName = "{} - {}".format(user,obj['nickname'])
                print("Checking:",documentName)

                try:
                    if firestore.Exists("Nicknames",documentName):
                        print("Skipping existing value!")
                        continue
                    else:
                        print("Adding new record:",documentName)
                    
                    firestore.AddData("Nicknames",documentName,obj)
                    print("Added:",obj['nickname'])
                except Exception as e:
                    print("Couldn't add {}, skipping.".format(documentName))
                    print(e)
                    

pushQuotes():
    with open('names.json') as f:
        data = json.loads(f.read())
        
        db = None

        firestore.init("../firebase.json")

        for user in data.keys():
            print(user)