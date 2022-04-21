"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
from operator import le

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

def getOutgoingCallersWithoutIncomingCalls(calls):
    outGoingCallers = []
    receivers = [row[1] for row in calls]
    for record in calls:
        if record[0] not in receivers:
            if record[0] not in outGoingCallers:
                outGoingCallers.append(record[0])

    return outGoingCallers

def getOutgoingCallersWithoutTexts(callers, texts):
    telemarketers = set()

    for number in callers:
        for item in texts:
            if number in item:
                break
            else:
                telemarketers.add(number)

    return telemarketers

def getPossibleTelemarketers():
    callersWithoutIncoming = getOutgoingCallersWithoutIncomingCalls(calls)
    possibleTeleMarketers = getOutgoingCallersWithoutTexts(callersWithoutIncoming, texts)

    return possibleTeleMarketers

possibleTeleMarketers = sorted(getPossibleTelemarketers())
print("These numbers could be telemarketers: ")
for number in possibleTeleMarketers:
    print(number)
