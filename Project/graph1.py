import pandas as pd
import matplotlib.pyplot as plt

file_path = "Survey_Raw_Data.csv"
#Loading file
df = pd.read_csv(file_path)

#Counting occurences
sleep_duration_counts = df['Sleep Duration'].value_counts()

#Index
sleep_duration_counts = sleep_duration_counts.sort_index()

# Plotting the bar chart
plt.figure(figsize=(10, 8))
plt.bar(sleep_duration_counts.index, sleep_duration_counts.values, color='skyblue', edgecolor='black')

plt.title('Frequency of Sleep Duration Ranges')
plt.xlabel('Sleep Duration')
plt.ylabel('Frequency')
plt.xticks(rotation=45, ha="right")  # Rotate labels to avoid overlap

plt.tight_layout()  # Adjust layout to make room for the rotated x-axis labels
plt.show()