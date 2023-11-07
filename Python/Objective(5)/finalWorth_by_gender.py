import pandas as pd
import matplotlib.pyplot as plt
#loading dataset into Pandas DataFrame
df = pd.read_csv('Billionaires Statistics Dataset.csv')

#Visualization 5 : Final Worth by Gender
#Create a boxplot chart to visualize the trend of Final Worth by Gender
plt.figure(figsize=(10, 6))
df.boxplot(column='finalWorth', by='gender')

#display chart
plt.title('Final Worth by Gender')
plt.xlabel('Gender')
plt.ylabel('Final Worth (Million)')
plt.suptitle('')  # Remove the default title
plt.show()