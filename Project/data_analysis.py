import pandas as pd
import matplotlib.pyplot as plt

# Function to convert sleep range to its midpoint
def range_to_midpoint(sleep_range):
    range_midpoints = {
        "0 - 30 mins": 0.25,
        "1hr - 1hr 30 mins": 1.25,
        "3 hrs 30 mins - 4 hrs": 3.75,
        "4 hrs - 4 hrs 30 mins": 4.25,
        "4 hrs 30 mins - 5 hrs": 4.75,
        "5 hrs - 5 hrs 30 mins": 5.25,
        "5 hrs 30 mins - 6 hrs": 5.75,
        "6 hrs - 6 hrs 30 mins": 6.25,
        "6 hrs 30 mins - 7 hrs": 6.75,
        "7 hrs - 7 hrs 30 mins": 7.25,
        "7 hrs 30 mins - 8 hrs": 7.75,
        "8 hrs - 8 hrs 30 mins": 8.25,
        "8 hrs 30 mins - 9 hrs": 8.75,
        "9 hrs - 9 hrs 30 mins": 9.25
    }
    return range_midpoints.get(sleep_range, 0) # Returns 0 if range not found


file_path = "Survey_Raw_Data.csv"

#Loading file

df = pd.read_csv(file_path)






# Convert sleep ranges to midpoints
df['Sleep Midpoint'] = df['Sleep Duration'].apply(range_to_midpoint)

# Plot the histogram
#plt.hist(df['Sleep Midpoint'], bins=len(df['Sleep Midpoint'].unique()), edgecolor='black')
#plt.title('Distribution of Sleep Duration')
#plt.xlabel('Hours of Sleep')
#plt.ylabel('Frequency')
#plt.show()

#Average and standard deviation
average_sleep_duration = df['Sleep Midpoint'].mean()
std_dev_sleep_duration = df['Sleep Midpoint'].std()

mean = average_sleep_duration 
std = std_dev_sleep_duration 

print(f"Average Sleep Duration: {average_sleep_duration} hours")
print(f"Standard Deviation of Sleep Duration: {std_dev_sleep_duration} hours")



# Calculate the percentages within 1σ, 2σ, and 3σ
within_1_std = ((df['Sleep Midpoint'] > (mean - std)) & (df['Sleep Midpoint'] < (mean + std))).mean()
within_2_std = ((df['Sleep Midpoint'] > (mean - 2*std)) & (df['Sleep Midpoint'] < (mean + 2*std))).mean()
within_3_std = ((df['Sleep Midpoint'] > (mean - 3*std)) & (df['Sleep Midpoint'] < (mean + 3*std))).mean()


print(f"Percentage within 1 standard deviation: {within_1_std * 100:.2f}% (Expected ~68%)")
print(f"Percentage within 2 standard deviations: {within_2_std * 100:.2f}% (Expected ~95%)")
print(f"Percentage within 3 standard deviations: {within_3_std * 100:.2f}% (Expected ~99.7%)")

# Determine the fraction of data within [mean - std, mean + std]
fraction_within_1_std = within_1_std
print(f"Fraction of data within 1 standard deviation: {fraction_within_1_std * 100:.2f}%")

# Assessing consistency with normal distribution
# A dataset is consistent with a normal distribution if the actual percentages are close to the expected values.
is_consistent = "Yes" if (within_1_std >= 0.68 and within_2_std >= 0.95 and within_3_std >= 0.997) else "No"
print(f"Is the distribution consistent with normal data? {is_consistent}")
