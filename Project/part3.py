import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 
from scipy.stats import norm

file_path = "Survey_Raw_Data.csv"
#Loading file
df = pd.read_csv(file_path)

#Midpoint
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

df['Sleep Midpoint'] = df['Sleep Duration'].apply(range_to_midpoint)

#Counting occurences
sleep_duration_counts = df['Sleep Duration'].value_counts()

#Index
sleep_duration_counts = sleep_duration_counts.sort_index()

#Q1: Dividing the interval
a = df['Sleep Midpoint'].min() - 0.1  # a little less than the minimum
b = df['Sleep Midpoint'].max() + 0.1  # a little more than the maximum
m = 30  # Number of subintervals

# Calculate the width of each subinterval
delta_x = (b - a) / m

# List of endpoints
x_i = [a + i*delta_x for i in range(m+1)]

print (x_i)
#Q2

 # Cumulative distribution values for each x_i
F_x_i = [df['Sleep Midpoint'][df['Sleep Midpoint'] <= x].count() / len(df['Sleep Midpoint']) for x in x_i]

#Q3
#Plotting values
plt.plot(x_i, F_x_i, marker='o')
plt.title('Cumulative Distribution Function (CDF)')
plt.xlabel('x_i')
plt.ylabel('F(x_i)')
plt.grid(True)
plt.show()

#Q4
#Approximate PDF
# Approximate f'(x_i) 
F_prime_x_i = [(F_x_i[i+1] - F_x_i[i-1]) / (2*delta_x) for i in range(1, m)]

#Q5 Approximate PDF plot
plt.plot(x_i[1:-1], F_prime_x_i, marker='o')
plt.title('Approximated Probability Density Function (PDF)')
plt.xlabel('x_i')
plt.ylabel("Approximated f'(x_i)")
plt.grid(True)
plt.show()


#Average and standard deviation
average_sleep_duration = df['Sleep Midpoint'].mean()
std_dev_sleep_duration = df['Sleep Midpoint'].std()

mean = average_sleep_duration 
std = std_dev_sleep_duration 


#Q6
#Superimposing Normal Distribution
# Generate points for the normal PDF
x_norm = np.linspace(a, b, 300)
y_norm = norm.pdf(x_norm, mean, std)

# Plot the approximated PDF and the normal PDF
plt.plot(x_i[1:-1], F_prime_x_i, marker='o', label='Empirical PDF')
plt.plot(x_norm, y_norm, label='Theoretical Normal PDF', linestyle='--')
plt.title('Empirical vs. Theoretical Normal PDF')
plt.xlabel('x')
plt.ylabel("Density")
plt.legend()
plt.grid(True)
plt.show()