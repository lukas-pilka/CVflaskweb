from google.cloud import firestore
db = firestore.Client()

collection_ref = db.collection(u'cvitems').get()
cvitems = list(doc.to_dict() for doc in collection_ref)


# counts days between dateFrom and dateTo and adds sum to dict
import datetime

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

# Searches from oldest dateFrom and sets like a history start date

historyStartDate = now
for i in cvitems:
    for event in i.values():
        dateFrom = event.get('dateFrom', now)
        dateFrom = dateFrom.date()
        if dateFrom < historyStartDate:
            historyStartDate = dateFrom

HistoryDaysCount = now - historyStartDate
HistoryDaysCount = HistoryDaysCount.days

# flask routing

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def root():

    return render_template('index.html', cvitems=cvitems, historyStartDate=historyStartDate, now=now, HistoryDaysCount=HistoryDaysCount)


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    # Flask's development server will automatically serve static files in
    # the "static" directory. See:
    # http://flask.pocoo.org/docs/1.0/quickstart/#static-files. Once deployed,
    # App Engine itself will serve those files as configured in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)