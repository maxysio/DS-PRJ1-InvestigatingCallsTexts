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
call_records = {}
for call in calls:
  if call[0] in call_records:
    call_records[call[0]] += int(call[3])
  else:
    call_records[call[0]] = int(call[3])
  
  if call[1] in call_records:
    call_records[call[1]] += int(call[3])
  else:
    call_records[call[1]] = int(call[3])
    
# Sort and get the first one
sorted_cr = [(k, call_records[k]) for k in sorted(call_records, key=call_records.get, reverse=True)]

#Print
print('{}  spent the longest time, {} seconds, on the phone during September 2016.'.format(sorted_cr[0][0], sorted_cr[0][1]))
