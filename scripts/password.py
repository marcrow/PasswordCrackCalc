import numpy as np
import matplotlib.pyplot as plt


# User variables
password_size = 8
char_set_size = 62  # 26 letters (lower) + 26 letters (upper) + 10 digits
tests_per_second_single = 1000000000  # 1M tests/sec


# Program variables
complexity = char_set_size**password_size 
second = {"second": 1, "text": "Second", "next": 60}
minute = {"second": 60, "text": "Minute", "next": 60}
hour = {"second": 3600, "text": "Hour", "next": 24}
day = {"second": 86400, "text": "Day", "next": 7}
week = {"second": 604800, "text": "Week", "next": 4}
month = {"second": 2592000, "text": "Month", "next": 12}
year = {"second": 31536000, "text": "Year", "next": 100}
century = {"second": 3153600000, "text": "Century"}

scale = [second, minute, hour, day, week, month, year, century]

# Set the scale
used_scale = century
for s in scale:
    proba = float((tests_per_second_single * s["second"] * s["next"]) / complexity)
    if proba > 0.95:
        used_scale = s
        break

# adjust the scale
time_single_short = np.linspace(0, used_scale["second"] * used_scale["next"], 1000)
probabilities = 1 - np.exp(-tests_per_second_single * time_single_short / complexity)

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(time_single_short / used_scale["second"], probabilities, label='Success Probability')

plt.xlabel(f'Time ({used_scale["text"]})')
plt.ylabel('Success Probability')
plt.title('Success Probability for Brute Force Attack based on Time')
plt.grid(True)
plt.xlim(0, used_scale["next"])
plt.ylim(0, 1)
plt.legend()
plt.show()