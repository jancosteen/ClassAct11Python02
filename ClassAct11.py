import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

sample_data = pd.read_csv('tips.csv')

#add calculated column
sample_data['tip_percentage']= sample_data['tip']/sample_data['total_bill']*100
print("Added Calculated Column")
print(sample_data)

#add subset of data
smoker = sample_data[sample_data.smoker == 'Yes']
non_smoker = sample_data[sample_data.smoker == 'No']
print('Smoker Subset')
print(smoker)

#correlation coefficient
print('Correlation Coefficient:')
corr = sample_data['total_bill'].corr(sample_data['tip'])
print(corr)
print('No significant correlation exist between Total_Bill and Tip amount')

#Visualisation of total tips of male vs female
plt.xlabel('Day of the Week')
plt.ylabel('Total Tips')

plt.bar(smoker.day,smoker.tip, color='r', label='Smoker', width=0.7)
plt.bar(non_smoker.day, non_smoker.tip, color='b', label="Non-Smoker", width=0.6)
plt.legend()
plt.show()


