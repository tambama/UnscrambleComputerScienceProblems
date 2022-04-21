"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
from time import perf_counter

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

def isFixedLine(tel):
  return tel[:2] == "(0"

def isBangaloreFixedLine(tel):
  return tel[:5] == "(080)"

def getAreaCode(tel):
  code = "("
  
  for character in tel[1:]:
    code += character
    if character == ')':
      return code

def isMobileNumber(tel):
  firstDigit = tel[0]
  if firstDigit != '7' and firstDigit != '8' and firstDigit != '9':
    return False

  if ' ' in tel:
    return True

def getMobilePrefix(tel):
  return tel[:4]

def isTeleMarketerNumber(tel):
  firstThreeDigits = tel[:3]
  return firstThreeDigits == "140" and ' ' not in tel

def getUniqueCodesCalledFromBangalore():
  numbers = []
  for record in calls:
    if not isBangaloreFixedLine(record[0]):
      continue
    
    calledNumber = record[1]
    if isTeleMarketerNumber(calledNumber):
      if "140" not in numbers:
        numbers.append("140")
    elif isBangaloreFixedLine(calledNumber):
      if "(080)" not in numbers:
        numbers.append("(080)")
    elif isMobileNumber(calledNumber):
      mobileCode = getMobilePrefix(calledNumber)
      if mobileCode not in numbers:
        numbers.append(mobileCode)
        
  return numbers

def getAllNumbersCalledFromBangalore():
  numbers = []
  for record in calls:
    if isBangaloreFixedLine(record[0]):
      calledNumber = record[1]
      if isTeleMarketerNumber(calledNumber):
          numbers.append("140")
      elif isBangaloreFixedLine(calledNumber):
          numbers.append("(080)")
      elif isMobileNumber(calledNumber):
        mobileCode = getMobilePrefix(calledNumber)
        numbers.append(mobileCode)
  return numbers

def getPercentageCallsToBangaloreNumbers():
  numbersCalled = getAllNumbersCalledFromBangalore()
  totalNumbers = len(numbersCalled)

  totalBangaloreCalled = 0
  for code in numbersCalled:
    if code == "(080)":
      totalBangaloreCalled += 1
  
  return (totalBangaloreCalled / totalNumbers) * 100


print ("The numbers called by people in Bangalore have codes: ")
orderedCodes = sorted(getUniqueCodesCalledFromBangalore())
for code in orderedCodes:
  print(code)

percentage = getPercentageCallsToBangaloreNumbers()
print("{:.2f}".format(percentage) + " percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")

