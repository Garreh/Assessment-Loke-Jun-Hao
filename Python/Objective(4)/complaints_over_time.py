import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('credit_card_complaints.csv')
#Visualization 4 : Credit Card Complaints Over Time

# Convert the 'date_received' column to a datetime format
data['date_received'] = pd.to_datetime(data['date_received'])

# Group complaints by year and count the number of complaints per year
complaints_over_time = data.groupby(data['date_received'].dt.to_period('y')).size()

# Create a line chart to visualize the trend of complaints over time
plt.figure(figsize=(12, 6))
complaints_over_time.plot(kind='line', marker='o')
plt.xlabel('Date')
plt.ylabel('Number of Complaints')
plt.title('Credit Card Complaints Over Time')
plt.grid(True)

# Annotate data points with the number of complaints
for i, count in enumerate(complaints_over_time):
    plt.annotate(str(count), (complaints_over_time.index[i].to_timestamp(), count), ha='center', va='bottom')

# Show the chart
plt.tight_layout()
plt.xticks(rotation=45)
plt.show()