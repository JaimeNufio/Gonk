

from pypresence import Presence
import time

import os
import datetime
import git
import json

client_id = "client_id" 

with open("credentials.json") as f:
  client_id = json.loads(f.read())['client_id']

RPC = Presence(client_id=client_id)
RPC.connect()

repo = git.Repo(os.getcwd())
master = repo.head.reference
lastcommit = master.commit.message

song = []
with open("./extras/Song.txt",'r') as f:
  for line in f:
    if line != "\n":
      song.append(line)
      print(line)

while 1:
  
  for line in song:
    RPC.update(
      buttons=[
      {"label": "Ehe", "url": "https://www.youtube.com/watch?v=yXQViqx6GMY"}, 
      # {"label": "Server", "url": "https://youtube.com"}
      ],
      large_image="gonkk",
      small_image="icon",
      details=line#"Last Commit: "+lastcommit
    )
    time.sleep(15) #Can only update presence every 15 seconds