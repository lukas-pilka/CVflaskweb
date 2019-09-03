import datetime
from datetime import date
from google.cloud import firestore

db = firestore.Client()

collection_ref = db.collection(u'cvitems').get()
cvitems = list(doc.to_dict() for doc in collection_ref)

# counts days between dateFrom and dateTo and adds sum to dict

now = datetime.date.today()

for i in cvitems:
    for event in i.values():
        dateFrom = event.get('dateFrom', 0)
        dateFrom = dateFrom.date()
        dateTo = event.get('dateTo')
        if dateTo != None:
            dateTo = dateTo.date()
        else:
            dateTo = now
        daysCount = dateTo - dateFrom
        event["dayscount"] = daysCount.days

historyStartDate = now
for i in cvitems:
    for event in i.values():
        dateFrom = event.get('dateFrom', now)
        dateFrom = dateFrom.date()
        if dateFrom < historyStartDate:
            historyStartDate = dateFrom

print(historyStartDate)

HistoryDaysCount = now - historyStartDate
HistoryDaysCount = HistoryDaysCount.days
print(HistoryDaysCount)