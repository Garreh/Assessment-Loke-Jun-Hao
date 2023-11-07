import matplotlib.pyplot as plt
import pandas as pd
#loading dataset into Pandas DataFrame
df = pd.read_csv('credit_card_complaints.csv')

#Visualization 1 : Company Response to Consumer
#Create a bar chart to visualize the trend of Company Reponse to Consumer
response_counts = df['company_response_to_consumer'].value_counts()
response_counts.plot(kind='bar')

#Annotate data points with the number of complaints
for i, count in enumerate(response_counts):
    plt.text(i, count, str(count), ha='center', va='bottom')

#display chart
plt.title('Company Response to Consumer')
plt.xlabel('Response Type')
plt.ylabel('Count of Complaints')
plt.grid(True)
plt.show()