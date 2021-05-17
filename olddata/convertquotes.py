import json

obj = {}

with open("olddata\quotes.json",'r',encoding="utf8",errors="ignore") as f:
    
    obj = json.load(f) #Load the old nickname list

place = {}

print(obj)


with open("records\quotes.json",'r') as where:

    place = json.load(where) #Load the target location

print(place)
print(type(place))
print(place.keys())

with open("records\quotes.json",'w') as where:

    for quote in obj.keys():
        user = obj[quote]
        print(user)

        if 'all' not in place:
            place['all'] = {}

        if user not in place['all'].keys():
            place['all'][user] = []
            
        quoteObj = {
            "quote":quote,
            "context":"",
            "chronicler":"",
            "when":"",
            "where":""
        }
        print(quoteObj)
        place['all'][user].append(quoteObj)

    print(place)
    json.dump(place,where,indent=2)
    