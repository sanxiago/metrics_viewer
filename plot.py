import sys
import pandas as pd
import matplotlib.pyplot as plt
import re

df = pd.read_csv(sys.argv[1])

# convert time into date
df['time'] = pd.to_datetime(df['time'], unit='ms')

separate_charts = False
interactive_charts = True
save_charts = True

field_filter = ':(EventType|RateUnit)$'

# Convert Count to deltas:
for metric in df.columns.values:
    m = re.search(":Count$",metric) # if metric ends with Count we convert to deltas
    if m:
        df[metric]=df[metric].diff().shift(-1)
        next
    m = re.search(field_filter,metric) # if metric ends with Count we convert to deltas
    if m:
        df = df.drop(metric, axis='columns')
# Plot DF 

plt.rc('legend', fontsize=6)

for metric in df.columns.values:
    if metric == 'time':
        x = df['time']
        plt.figure(sys.argv[1]).set_figwidth(16)
        next
    else:
        y = df[metric]
        plt.plot(x,y, label=metric)
        plt.legend(bbox_to_anchor=(0.4, 1.15), loc='upper center')
        

# beautify the x-labels
plt.gcf().autofmt_xdate()

if interactive_charts:
   plt.show()


