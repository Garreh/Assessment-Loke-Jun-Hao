import pandas as pd
import matplotlib.pyplot as plt
#loading dataset into Pandas DataFrame
df = pd.read_csv('Billionaires Statistics Dataset.csv')

#Visualization 4 : Average Final Worth by Category
#Create a bar chart to visualize the trend of Average Final Worth by Category
category_final_worth = df.groupby('category')['finalWorth'].mean()
category_final_worth.plot(kind='bar', figsize=(10, 6))

#display chart
plt.xlabel('Category')
plt.ylabel('Average Final Worth (Million)')
plt.title('Average Final Worth by Category')
plt.xticks(rotation=45)
plt.show()