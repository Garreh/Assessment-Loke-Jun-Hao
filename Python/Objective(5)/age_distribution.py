import pandas as pd
import matplotlib.pyplot as plt
#loading dataset into Pandas DataFrame
df = pd.read_csv('Billionaires Statistics Dataset.csv')

#Visualization 1 : Age Distribution
#Create a plot chart to visualize the trend of Age Distribution
plt.figure(figsize=(10, 6))
df['age'].plot(kind='hist', bins=20, edgecolor='k')

#display chart
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Age Distribution')
plt.show()