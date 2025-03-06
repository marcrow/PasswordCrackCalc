import numpy as np
import matplotlib.pyplot as plt
from collections import deque

# User config
T_total = 60 * 10    # total time (s)
R_gen = 2.0             # tokens generated per second
r_bf = 1/9              # brute force rate (attempts/s)
N = 10000               # total code space
max_tokens = 10000      # max valid tokens
T_life = 0              # token expiration time (0 = no expiration)

time_values = np.arange(0, T_total+1)
p_fail = np.ones(len(time_values))
p_fail[0] = 1.0

q = deque()  # store creation times
bf_left = 0.0  # leftover fraction

for i in range(1, len(time_values)):
    t = time_values[i]

    # remove expired
    if T_life > 0:
        while q and (t - q[0] >= T_life):
            q.popleft()

    # generate tokens
    nb_new = R_gen
    while nb_new > 0 and len(q) < max_tokens:
        q.append(t)
        nb_new -= 1

    nb_valid = len(q)

    # brute force attempts
    bf_left += r_bf
    attempts = int(np.floor(bf_left))
    bf_left -= attempts

    if attempts > 0:
        p_fail_here = (1 - nb_valid / N)**attempts
        p_fail[i] = p_fail[i-1] * p_fail_here
    else:
        p_fail[i] = p_fail[i-1]

p_success = 1 - p_fail

plt.plot(time_values, p_success)
plt.xlabel('Time (s)')
plt.ylabel('Success Probability')
plt.title('Probability of Successful Token Brute Force Attack Over Time')
plt.grid(True)
plt.show()
