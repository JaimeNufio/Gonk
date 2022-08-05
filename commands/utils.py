import json
from datetime import datetime
from dateutil import parser

def options(string,option,value="",values=[]):
    #todo, handle values passed with options

    parts = string.lower().split(" ")

    for part in parts:
        if part == option and value == "":
            return True

    if value != "":
        #TODO
        print("Option found, Value not 0")
        return True
    
    return False

#deprecate?
def gatherUserByID(userID):
    temp = {}
    userID=str(userID)
    
    with open("././records/names.json","r") as file: 

        temp = json.load(file)

    collected = []
    collectedReasons = []

    for guild in temp.keys():
        print("Guild:",guild)
        print()
        if userID in temp[guild].keys():
            print("NN list")
            print(temp[guild][userID]['nicknames'])
            for nickname in temp[guild][userID]['nicknames']:
                collected.append(nickname)
            for reason in temp[guild][userID]['reasons']:
                collectedReasons.append(reason)

    for i in collected:
        print(i)
    return [collected,collectedReasons]

def prettydate(x):
    if not x or x == "":
        return "Date Not Found"

    dt = parser.parse(x)

    pretty = "{}/{}/{} {}:{}".format(dt.month,dt.day,dt.year,dt.hour,dt.min)
    print(pretty)
    return pretty

#just a wrapper for the json.load function
def returnText(file):

    temp = ""
    
    with open("././records/{}.json".format(file),"r") as file: 

        temp = json.load(file)
        
    return temp
