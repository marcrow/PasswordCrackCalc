#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt

# === User Parameters ===
code_length = 4            # Number of digits in the code
character_set_size = 10     # Size of the character set (0-9 for a 4-digit code)
attempts_per_second = 1/3   # One attempt every 3 seconds
mode = "probabilistic"      # Choose "deterministic" or "probabilistic"

# === Computed Variables ===
total_combinations = character_set_size ** code_length  # Total number of possible codes
max_time_seconds = total_combinations / attempts_per_second  # Max time to test all combinations

# === Time Scale Definitions ===
time_scales = [
    {"unit": "Second", "factor": 1, "limit": 60},
    {"unit": "Minute", "factor": 60, "limit": 60},
    {"unit": "Hour", "factor": 3600, "limit": 24},
    {"unit": "Day", "factor": 86400, "limit": 7},
    {"unit": "Week", "factor": 604800, "limit": 4},
    {"unit": "Month", "factor": 2592000, "limit": 12},
    {"unit": "Year", "factor": 31536000, "limit": 100},
]

# Select the most appropriate time scale
selected_time_scale = time_scales[-1]  # Default: Century
for scale in time_scales:
    if max_time_seconds / scale["factor"] < scale["limit"]:
        selected_time_scale = scale
        break

# === Probability Calculation ===
time_intervals = np.linspace(0, max_time_seconds, 1000)  # Time range

if mode == "probabilistic":
    success_probabilities = 1 - np.exp(-attempts_per_second * time_intervals / total_combinations)  # Exponential model
elif mode == "deterministic":
    success_probabilities = time_intervals / max_time_seconds  # Linear model
    success_probabilities[success_probabilities > 1] = 1  # Cap at 100%

# === Plot the Graph ===
plt.figure(figsize=(10, 6))
plt.plot(time_intervals / selected_time_scale["factor"], success_probabilities, label=f'Success Probability ({mode.capitalize()})')

plt.xlabel(f'Time ({selected_time_scale["unit"]})')
plt.ylabel('Success Probability')
plt.title('Success Probability for Brute Force Attack based on Time')
plt.grid(True)
plt.xlim(0, max_time_seconds / selected_time_scale["factor"])
plt.ylim(0, 1)
plt.legend()
plt.show()
