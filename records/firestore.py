from typing import final
import firebase_admin
import json
import os
import random

from google.cloud import firestore
from firebase_admin import credentials


db = None

def init(path):

    global db

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
    except Exception:
        print("Attempt to query failed!")
        print(Exception)

    print("Database accessed sucessfully; should be good to go!")

def AddData(collection,documentName,data):

    doc_ref = db.collection(collection).document(documentName)

    data['id'] = GetMetaCount(collection)
    doc_ref.set(data)
    return UpdateMetaCount(collection,1)

def GetMetaCount(collection):

    doc_ref = db.collection(collection).document(u'META').get()
    
    if doc_ref.exists:
        return doc_ref.to_dict()['count']
    else:
        print("failed to read META for collection {}".format(collection))
        return -1


#keeping track of the count of records in document
def UpdateMetaCount(collection,delta=0):

    print("Updating Collection: {}".format(collection))
    count = GetMetaCount(collection)

    doc_ref = db.collection(collection).document('META')
    doc_ref.update({'count':count+delta})

    return count+delta

def GetQuotes(guild,who=None):
    
    count = GetMetaCount("Quotes")
    Quotes = db.collection('Quotes')

    if who != None:
        x = Quotes.where('author','==',who).get()
        if len(x) > 0:
            x = random.choice(x)
        else:
            x = None
    else:
        x = Quotes.where('guild','==',guild).where('id','==',random.choice(range(count+1))).limit(1).get()[0]

    print(x)
    return x