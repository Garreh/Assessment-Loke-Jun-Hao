import pandas as pd
import matplotlib.pyplot as plt
#loading dataset into Pandas DataFrame
df = pd.read_csv('Billionaires Statistics Dataset.csv')

#Visualization 6 : Source of Wealth by Gender
#Create a bar chart to visualize the trend of Source of Wealth by Gender
source_gender_counts = df.groupby(['category', 'gender']).size().unstack()
source_gender_counts.plot(kind='bar', stacked=True, figsize=(10, 6))

#display chart
plt.title('Source of Wealth by Gender')
plt.xlabel('Source')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()