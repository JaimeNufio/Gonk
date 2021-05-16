import json

obj = {}

with open("olddata/nicknames.json",'r',encoding="utf8",errors="ignore") as f:
    
    obj = json.load(f) #Load the old nickname list

place = {}


with open("records/names.json",'r') as where:

    place = json.load(where) #Load the target location

print(place)
print(type(place))
print(place.keys())

with open("records/names.json",'w') as where:

    for user in obj.keys():

        if user not in place.keys():
            place[user] = []

        for nickname in obj[user]:
            nicknameObj = {
                "nickname":nickname,
                "reason":"",
                "renamer":0,
                "when":"",
                "serverid":"",
                "servername":""
            }

            place[user].append(nicknameObj)

    print(place)
    json.dump(place,where,indent=2)
    