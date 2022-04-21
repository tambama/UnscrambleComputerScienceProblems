"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

def getLongestCall():
    
    totals = {}
    for record in calls:
        if record[0] not in totals:
            totals[record[0]] = int(record[3])
        else:
            totals[record[0]] += int(record[3])

        if record[1] not in totals:
            totals[record[1]] = int(record[3])
        else:
            totals[record[1]] += int(record[3])

    first_key = list(totals)[0]

    longestCall = [first_key, totals[first_key]]

    for key in totals:
        if int(totals[key]) > int(longestCall[1]):
            longestCall = [key, totals[key]]
    
    return longestCall

longestCall = getLongestCall()

print(longestCall[0] + " spent the longest time, " + str(longestCall[1]) + " seconds, on the phone during September 2016.")