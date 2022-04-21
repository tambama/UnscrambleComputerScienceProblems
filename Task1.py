"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
from itertools import count
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
    telephoneNumbers = []
    for record in texts:
        if record[0] in telephoneNumbers:
            continue
        else:
            telephoneNumbers.append(record[0])
        
        if record[1] in telephoneNumbers:
            continue
        else:
            telephoneNumbers.append(record[1])

    for record in calls:
        if record[0] in telephoneNumbers:
            continue
        else:
            telephoneNumbers.append(record[0])
        
        if record[1] in telephoneNumbers:
            continue
        else:
            telephoneNumbers.append(record[1])

    return telephoneNumbers

count = len(getUniqueTelephoneNumbers())
print("There are " + str(count) + " different telephone numbers in the records.")