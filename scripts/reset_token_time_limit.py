#!/usr/bin/env python
# This script is used to calculate the optimal transition from token generation to brute force
# It is focused on the reset token time limit
import numpy as np
import matplotlib.pyplot as plt

# User variables
T_total = 60 * 2  # Lifetime of the token in seconds
R_gen = 100  # Token generation rate (nb token per second)
r = 200  # Brute-force rate (nb attempts per second)
password_size = 6
char_set_size = 36  # 26 letters (lower) + 10 digits
max_tokens = 1000  # Maximum number of tokens generated. Comment this line to disable the limit

# Program variables
N = char_set_size**password_size  

# Range for T_gen
T_gen_values = np.linspace(0, T_total, 300)

# Calculate the probability of success for each T_gen
P_success_values = []
for T_gen in T_gen_values:
    g = 0
    try:
        if max_tokens is not None:
            g = min(T_gen * R_gen, max_tokens)
        else:
            g = T_gen * R_gen  # Number of tokens generated
    except NameError:
        g = T_gen * R_gen  # Number of tokens generated if max_tokens is not defined
    T_bf = T_total - T_gen  # Time left for brute-force
    P_success = 1 - (1 - g/N)**(r * T_bf)
    P_success_values.append(P_success)

# Plotting the curve
plt.figure(figsize=(10, 6))
plt.plot(T_gen_values, P_success_values, label='Probability of Success')

plt.xlabel('Time Spent Generating Tokens (seconds)')
plt.ylabel('Probability of Success')
plt.title('Optimal Transition from Token Generation to Brute Force')
plt.grid(True)
plt.show()
