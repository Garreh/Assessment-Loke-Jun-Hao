import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('credit_card_complaints.csv')

#Visualization 2 : Top 10 Companies with Most Complaints
#Create a bar chart to visualize the trend of Top 10 Companies with Most Complaints
company_counts = df['company'].value_counts()
company_counts[:10].plot(kind='bar', figsize=(10, 6))

#Annotate data points with the number of complaints
for i, count in enumerate(company_counts):
    plt.text(i, count, str(count), ha='center', va='bottom')

#display chart
plt.title('Top 10 Companies with Most Complaints')
plt.xlabel('Company')
plt.ylabel('Count of Complaints')
plt.grid(True)
plt.xticks(rotation=45)
plt.show()