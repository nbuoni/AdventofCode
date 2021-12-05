# loads list of ocean depths detected by a sonar sweep
from constants import depths

# creates a new list containing the sums of a three-measurement sliding window

depths_three_sum = []
for x in range(2, len(depths)):
		depths_three_sum.append(depths[x] + depths[x-1] + depths[x-2])

# counts the number of times the sum of measurements in this sliding window increases
number_of_increases = 0
for x in range(len(depths_three_sum) - 1):
    if depths_three_sum[x] > depths_three_sum[x-1]:
        number_of_increases += 1
print(number_of_increases)


