import matplotlib.pyplot as plt
import pandas as pd
#loading dataset into Pandas DataFrame
df = pd.read_csv('credit_card_complaints.csv')

#Visualization 3 : Complants Count by State
#Create a bar chart to visualize the trend of complaints count by state
state_count = df['state'].value_counts()
state_count.plot(kind = 'bar', figsize = (10,6))
plt.title('Count of Complaints by State')
plt.xlabel('State')
plt.ylabel('Count of Complaints')

#Annotate data points with the number of complaints
for i, count in enumerate(state_count):
    plt.text(i, count, str(count), ha='center', va='bottom')

#display chart
plt.tight_layout()
#Changes the rotation of xlabel for ease of viewing
plt.xticks(rotation=90)
plt.show()