from typing import final
import firebase_admin
import json
import os

from google.cloud import firestore
from firebase_admin import credentials

def init(path):

    try:
        cred = credentials.Certificate(path)
        firebase_admin.initialize_app(cred)
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"]=path
    except e:
        print("Failed to connect to database!!!!")
        print(e)
        exit(1)

    print("initalized credentials.")

    try:
        db = firestore.Client()
        users_ref = db.collection(u'messages')
    except e:
        print("Attempt to query failed!")
        print(e)

    print("Database accessed sucessfully; should be good to go!")

def AddData(collection,documentName,data):

    # db = firestore.Client()
    # doc_ref = db.collection(u'messages').document(u'ah')
    # doc_ref.set({
    #     u'first': u'Ada',
    #     u'last': u'Lovelace',
    #     u'born': 1815
    # })

    db = firestore.Client()
    doc_ref = db.collection(collection).document(documentName)
    doc_ref.set(data)

# # Then query for documents
# users_ref = db.collection(u'messages')

# for doc in users_ref.stream():
#     print(u'{} => {}'.format(doc.id, doc.to_dict()))