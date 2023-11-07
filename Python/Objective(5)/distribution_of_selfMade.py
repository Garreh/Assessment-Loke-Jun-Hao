import pandas as pd
import matplotlib.pyplot as plt
#loading dataset into Pandas DataFrame
df = pd.read_csv('Billionaires Statistics Dataset.csv')
#Visualization 3 : Distribution of Self-Made Status
#Create a plot chart to visualize the trend of Distribution of Self-Made Status
self_made_counts = df['selfMade'].value_counts()
self_made_counts.plot(kind='pie', autopct='%1.1f%%', figsize=(6, 6))
#display chart
plt.title('Distribution of Self-Made Status')
plt.ylabel('')
plt.show()