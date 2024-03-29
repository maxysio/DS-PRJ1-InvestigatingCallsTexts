"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

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
in Bangalore.
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
# PART A

# Function to get Area Code
def getAreaCode(ph_no):
  areaCode = ''
  ph_no = str(ph_no)
  if(ph_no.startswith('140')):
    areaCode = '140'
  elif(ph_no.startswith('(')):
    idx_ending_parenthesis = ph_no.find(')')
    if(idx_ending_parenthesis>=0):
      areaCode = ph_no[1:idx_ending_parenthesis]
  elif(ph_no.find(' ')>=0):
    areaCode = ph_no[0:4]

  return areaCode

#Get the list of calls originating from Bangalore
calls_from_blore = [(x, y, z, v) for x, y, z, v in calls if(str(x).startswith('(080)'))]

# Get the area codes for the receiving numbers and create a unique set
area_codes = set()
for call in calls_from_blore:
  area_codes.add(getAreaCode(call[1]))

# Print the area codes of the receving numbers
print('The numbers called by people in Bangalore have codes:')
for ac in sorted(area_codes):
  print(ac)

# Part B
# Get the list of calls made from bangalore to bangalore
calls_from_blore_to_blore = [(x, y, z, v) for x, y, z, v in calls_from_blore if(str(y).startswith('(080)'))]

# Get the percentage of calls made from bangalore to bangalore
pct_blore_to_blore = round((len(calls_from_blore_to_blore)/len(calls_from_blore))*100, 2)
print('{} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.'.format(pct_blore_to_blore))
