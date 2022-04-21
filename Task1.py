"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
from itertools import count
from turtle import st
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

def getUniqueTelephoneNumbers():
    print("Texts: " + str(len(texts)) + ", Calls: " + str(len(calls)))
    telephoneNumbers = []
    for text in texts:
        if text[0] not in telephoneNumbers:
            telephoneNumbers.append(text[0])
        
        if text[1] not in telephoneNumbers:
            telephoneNumbers.append(text[1])

    for call in calls:
        if call[0] not in telephoneNumbers:
            telephoneNumbers.append(call[0])
        
        if call[1] not in telephoneNumbers:
            telephoneNumbers.append(call[1])

    return telephoneNumbers

count = len(getUniqueTelephoneNumbers())
print("There are " + str(count) + " different telephone numbers in the records.")