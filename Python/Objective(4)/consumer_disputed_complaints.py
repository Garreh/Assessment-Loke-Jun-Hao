
import matplotlib.pyplot as plt
import pandas as pd
#loading dataset into Pandas DataFrame
df = pd.read_csv('credit_card_complaints.csv')

#Visualization 6 : Consumer Disputed Complaints
#Create a pie chart to visualize the trend of Consumer Disputed Complaints
disputed_counts = df['consumer_disputed'].value_counts()
disputed_counts.plot(kind='pie', autopct='%1.1f%%', startangle=90, figsize=(6, 6))

#display chart
plt.title('Consumer Disputed Complaints')
plt.grid(True)
plt.show()