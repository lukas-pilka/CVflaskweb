import datetime
from datetime import date
from google.cloud import firestore

db = firestore.Client()

collection_ref = db.collection(u'cvitems').get()
cvitems = list(doc.to_dict() for doc in collection_ref)

now = datetime.datetime.now()
now = now.strftime("%Y, %m, %d")

for i in cvitems:
    for event in i.values():
        dateFrom = event.get('dateFrom', 0)
        dateTo = event.get('dateTo', now)
        print(dateFrom, dateTo)


dateFrom = date(2008, 8, 18)
dateTo = date(2008, 9, 18)
delta = dateTo - dateFrom
print(delta.days)