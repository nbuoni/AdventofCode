# Given a fabricated list of ocean depths detected by a sonar sweep, this counts the number of times a depth measurement increases from the previous measurement.
from constants import depths

number_of_increases = 0
for x in range(len(depths) - 1):
    if depths[x + 1] > depths[x]:
        number_of_increases += 1
print(number_of_increases)
