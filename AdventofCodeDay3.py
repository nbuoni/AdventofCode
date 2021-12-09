# import packages

import pandas as pd

# import submarine diagnostic report as pandas dataframe with one digit of bit per cell
submarine_bits = pd.read_csv(r'/Users/ninabuoni/Documents/AdventofCode/Advent of Code Day 3 Data.csv',
                             header = None,
                             index_col = False)

# define gamma rate and epsilon rate as empty strings
gamma_rate = ""
epsilon_rate = ""

#
"""  determine each bit in the gamma rate by finding most common bit in
corresponding position of all numbers in the diagnostic report and determine each
bit in the epsilon rate by finding least common bit in corresponding position of
all numbers in the diagnostic report"""

for i in range(len(submarine_bits.columns)):
    zero_count = 0
    one_count = 0

    for j in range(len(submarine_bits)):
        if submarine_bits.iloc[j,i] == 0:
            zero_count += 1
        else:
            one_count += 1

    if zero_count > one_count:
        gamma_rate = gamma_rate + '0'
        epsilon_rate = epsilon_rate + '1'

    else:
        gamma_rate = gamma_rate + '1'
        epsilon_rate = epsilon_rate + '0'

# print gamma rate and epsilon rate
print(f"gamma rate = {gamma_rate}")
print(f"epsilon rate= {epsilon_rate}")

# convert gamma rate and epsilon rate to decimal from binary
gamma_rate_decimal = int(gamma_rate, 2)
epsilon_rate_decimal = int(epsilon_rate, 2)

# calculate power consumption by multiplying gamma rate by epsilon rate
power_consumption = gamma_rate_decimal*epsilon_rate_decimal

# print power consumption
print(f"power_consumption= {power_consumption}")
