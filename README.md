# Gonk

Discord Bot for my personal Servers.

![alt text](https://raw.githubusercontent.com/JaimeNufio/Gonk/main/assets/loggedin.png)

## Usage:

Fill out credentialsExample.json:
- token -  your bot's toke
- guid_ids - list of servers you want the bot to care about, where it exists
- client_secret - your application's client secret
- client_id - your application's client id

Download requierements:
```pip install -r ./requirements.txt```

Start Bot:
```python3./__init__.py```


## New Features:
- Slash Commands 
- Multi-Server Support

## Command List:

### rename 

`/ rename user nickname [reason]`

Gives the ```user``` the nickname ```nickname``` in the server. Documenting with ```reason``` is optional. ```user``` may not give themselves a new nickname. 

### getnicknames

`/ getnicknames user`

Returns an array of known nicknames for selected user. Lists reasons if one exists.

### addquote

`/ addquote user quote [reason]`

Stores a new ```quote``` attributed to ```user```. Documenting with ```reason``` is optional.

### remindme

`/ addquote user quote [reason]`

Stores a new ```message``` to be sent in the channel the request was made at ```date```:```time```.

## Passive Commands:

The bot listens to incoming messages passively and will interact intermittently with users based on what regex strings it matches in read messages.

Data it collects are stored on Google Firebase.


