import pandas as pd
import matplotlib.pyplot as plt
#loading dataset into Pandas DataFrame
df = pd.read_csv('Billionaires Statistics Dataset.csv')

#Visualization 2 : Age vs. Final Worth
#Create a scatter chart to visualize the trend of Age vs. Final Worth
plt.figure(figsize=(10, 6))
df.plot.scatter(x='age', y='finalWorth', alpha=0.5)

#display chart
plt.xlabel('Age')
plt.ylabel('Final Worth (Million)')
plt.title('Age vs. Final Worth')
plt.show()
