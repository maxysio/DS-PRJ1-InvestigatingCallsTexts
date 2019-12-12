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

import pandas as pd

# Read the call data into a dataframe
df_calls = pd.DataFrame(calls, columns=['Calling_Number', 'Receiving_Number', 'Start_Time', 'Duration'])

# Read the text data into a dataframe
df_texts = pd.DataFrame(texts, columns=['Sending_Number', 'Receiving_Number', 'Timestamp'])

# Find phone numbers which make calls but never receive calls
df_tm = df_calls[~df_calls.Calling_Number.isin(df_calls.Receiving_Number)]

# Cross check the above list with the phone numbers which never sends or receives texts
df_tm = df_tm[~df_tm.Calling_Number.isin(df_texts.Sending_Number)]
df_tm = df_tm[~df_tm.Calling_Number.isin(df_texts.Receiving_Number)]

# Print the list of possible telemarketers
print('These numbers could be telemarketers: ')
for tm in np.sort(df_tm.Calling_Number.unique()):
  print(tm)
