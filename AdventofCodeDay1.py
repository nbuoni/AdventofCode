# Given a fabricated list of ocean depths detected by a sonar sweep, this counts the number of times a depth measurement increases from the previous measurement.
from constants import depths

y = 0
for x in range(1, len(depths)):
    if depths[x] > depths[x-1]:
        y += 1
print(y)
