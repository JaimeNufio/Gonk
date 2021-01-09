import json

def updateJSON(serverID,memberID,name):
    temp = {}
    
    with open("././records/names.json","r") as file: 

        temp = json.load(file)

    with open("././records/names.json","w") as file:


        if serverID not in temp.keys():
            temp[ serverID ] = {}

        if memberID not in temp[ serverID ].keys():
            temp[ serverID ][ memberID ] = {}

        if "nicknames" not in temp[ serverID ][ memberID ].keys():
            temp[ serverID ][ memberID ]['nicknames'] = []

        temp[ serverID ][ memberID ]['nicknames'].append( name )

        json.dump(temp,file,indent=2)

def gatherUserByID(userID):
    temp = {}
    
    with open("././records/names.json","r") as file: 

        temp = json.load(file)

    collected = []

    for guild in temp.keys():
        if userID in temp[guild].keys():
            for nickname in temp[guild][userID]['nicknames']:
                collected.append(nickname)

    for i in collected:
        print(collected)

gatherUserByID('memberID')
#updateJSON("serverID_1","memberID","nickname6")