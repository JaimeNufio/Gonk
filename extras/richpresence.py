

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



while 1:
  RPC.update(
    buttons=[
    {"label": "Repo", "url": "https://github.com/JaimeNufio/Gonk"}, 
    # {"label": "Server", "url": "https://youtube.com"}
    ],
    large_image="gonkk",
    small_image="icon",
    # details="",
    details="Last Commit: "+lastcommit
  )
  time.sleep(15) #Can only update presence every 15 seconds