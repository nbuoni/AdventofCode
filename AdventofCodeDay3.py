# import packages

import pandas as pd

# import submarine diagnostic report as pandas dataframe with one digit of bit per cell
submarine_bits = pd.read_csv(r'/Users/ninabuoni/Documents/AdventofCode/AdventofCodeDay3Data.csv',
                             header = None,
                             index_col = False)

# define function to obtain most common column value of data frame containing bits given data frame and column index
def get_most_common_value(df, column_index):
    ratio = submarine_bits[column_index].sum()/len(submarine_bits)
    most_common_value = round(ratio)
    return most_common_value

# define function to obtain least common column value of data frame containing bits given data frame and column index
def get_least_common_value(df, column_index):
    ratio = submarine_bits[column_index].sum()/len(submarine_bits)
    least_common_value = round(1- ratio)
    return least_common_value

"""  determine each bit in the gamma rate by finding most common bit in
corresponding position of all numbers in the diagnostic report and determine each
bit in the epsilon rate by finding least common bit in corresponding position of
all numbers in the diagnostic report"""

gamma_rate = "".join([str(get_most_common_value(submarine_bits, i)) for i in range(len(submarine_bits.columns))])
epsilon_rate = "".join([str(get_least_common_value(submarine_bits, i)) for i in range(len(submarine_bits.columns))])

# print gamma rate and epsilon rate
print(f"gamma rate = {gamma_rate}")
print(f"epsilon rate = {epsilon_rate}")

# convert gamma rate and epsilon rate to decimal from binary
gamma_rate_decimal = int(gamma_rate, 2)
epsilon_rate_decimal = int(epsilon_rate, 2)

# calculate power consumption by multiplying gamma rate by epsilon rate
power_consumption = gamma_rate_decimal*epsilon_rate_decimal

print(f"power_consumption= {power_consumption}")
