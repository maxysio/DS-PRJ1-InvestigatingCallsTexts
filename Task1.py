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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
def getPhoneNumbers(list_whole):
  list_phone_numbers = []
  for item in list_whole:
    arr_list = str(item).split(',')
    list_phone_numbers.append(arr_list[0])
    list_phone_numbers.append(arr_list[1])
  return list_phone_numbers
  
 combined_list = getPhoneNumbers(calls) + getPhoneNumbers(texts)
 combined_list = set(combined_list)
 print('There are {} different telephone numbers in the records'.format(len(combined_list)))