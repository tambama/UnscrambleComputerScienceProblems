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
    longestCall = calls[0]

    for record in calls:
        if int(record[3]) > int(longestCall[3]):
            longestCall = record
    
    return longestCall

longestCall = getLongestCall()

print(longestCall[0] + " spent the longest time, " + longestCall[3] + " seconds, on the phone during September 2016.")