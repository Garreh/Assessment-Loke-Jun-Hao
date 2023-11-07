import matplotlib.pyplot as plt
import pandas as pd
#loading dataset into Pandas DataFrame
df = pd.read_csv('credit_card_complaints.csv')

#Visualization 5 : Complaints by Submitted Via
#Create a bar chart to visualize the trend of Complaints by Submitted Via
submitted_via_counts = df['submitted_via'].value_counts()
submitted_via_counts.plot(kind='bar', figsize=(8, 6))

#Annotate data points with the number of complaints
for i, count in enumerate(submitted_via_counts):
    plt.text(i, count, str(count), ha='center', va='bottom')

# Show the chart
plt.title('Complaints by Submitted Via')
plt.xlabel('Submitted Via')
plt.ylabel('Count of Complaints')
plt.grid(True)
plt.xticks(rotation=90)
plt.show()