from google.cloud import datastore

datastore_client = datastore.Client()
import datetime
import os
import sys
sys.path.append(os.path.realpath('.'))
import inquirer

# Asks on category

categoryQuestions = [inquirer.List('choice', message='Category: ',choices=['Project', 'Article', 'Publication', 'Education', 'Job'],),]
categoryDict = inquirer.prompt(categoryQuestions)
category = categoryDict["choice"]

# Asks on subject

subject = input('Subject: ')
description = input('Description: ')
url = input('Url: ')

# Asks and formating date

dateFrom = input('Date from (MM-YYYY): ')
dateTo = input('Date to (MM-YYYY): ')

if dateFrom != '':
    dateFromObj = datetime.datetime.strptime(dateFrom, '%m-%Y')
else:
    dateFromObj = ''
if dateTo != '':
    dateToObj = datetime.datetime.strptime(dateTo, '%m-%Y')
else:
    dateToObj = ''

# Creates CVitem

cvItem = {
        "dateFrom": dateFromObj,
        "dateTo": dateToObj,
        "category": category,
        "subject": subject,
        "description": description,
        "url": url,
        }

# Writes only filled items

cvItemFilled = {}
for key, value in cvItem.items():
    if value != '':
        cvItemFilled[key] = value

# Writes CV item into database

def writeitem(eventName):
    entity = datastore.Entity(key=datastore_client.key('cvitems'))
    entity.update({
        'event': eventName
    })

    datastore_client.put(entity)

writeitem(cvItemFilled)

print('Passed:' + str(cvItemFilled))
