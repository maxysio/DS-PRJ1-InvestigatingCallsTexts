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
import pandas as pd

#Import the list to a dataframe
df_calls = pd.DataFrame(calls, columns=['Calling_Number', 'Receiving_Number', 'Start_Time', 'Duration'])

# Split it by making and receiving calls
df_CallingNumbers = df_calls.melt(id_vars=['Calling_Number'], value_vars=['Duration'], value_name='Duration')
df_CallingNumbers.rename(columns={'Calling_Number':'Phone_Number'}, inplace=True)
df_CallingNumbers.Duration = df_CallingNumbers.Duration.astype(int)

df_ReceivingNumbers = df_calls.melt(id_vars=['Receiving_Number'], value_vars=['Duration'], value_name='Duration')
df_ReceivingNumbers.rename(columns={'Receiving_Number':'Phone_Number'}, inplace=True)
df_ReceivingNumbers.Duration = df_ReceivingNumbers.Duration.astype(int)

# Combine the lists
df_CombinedNumbers = pd.concat([df_CallingNumbers, df_ReceivingNumbers], axis=0, sort=False)
df_CombinedNumbers.reset_index(inplace=True, drop=True)

# Group By and find the sum of all durations
df_GroupedNumbers = df_CombinedNumbers.groupby(['Phone_Number']).Duration.sum().reset_index()

# Sort and get the first one
df_GroupedNumbers.sort_values(by = ['Duration'], ascending=[False], inplace=True)
df_GroupedNumbers.reset_index(inplace=True, drop=True)

#Print
print('{}  spent the longest time, {} seconds, on the phone during September 2016.'.format(df_GroupedNumbers.Phone_Number[0], df_GroupedNumbers.Duration[0]))