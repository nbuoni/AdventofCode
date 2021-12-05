# loads list of ocean depths detected by a sonar sweep
from constants import depths

# creates a new list containing the sums of a three-measurement sliding window
third_depths = list()
for x in range(2, len(depths)):
		third_depths.append(depths[x] + depths[x-1] + depths[x-2])

# counts the number of times the sum of measurements in this sliding window increases
y = 0
for x in range(1, len(third_depths)):
    if third_depths[x] > third_depths[x-1]:
        y += 1
print(y)


