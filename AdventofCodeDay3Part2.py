# import packages

import pandas as pd
import math

# import submarine diagnostic report as pandas dataframe with one digit of bit per cell
submarine_bits = pd.read_csv(r'/Users/ninabuoni/Documents/AdventofCode/AdventofCodeDay3Data.csv',
                             header = None,
                             index_col = False)

# define function to obtain most common column value of data frame containing bits given data frame and column index
def get_most_common_value(df, column_index):
    ratio = submarine_bits[column_index].sum()/len(submarine_bits)
    if ratio >= 0.5:
        most_common_value = 1
    else:
        most_common_value = 0
    return most_common_value

# define function to obtain least common column value of data frame containing bits given data frame and column index
def get_least_common_value(df, column_index):
    ratio = submarine_bits[column_index].sum()/len(submarine_bits)
    if ratio >= 0.5:
        least_common_value = 0
    else:
        least_common_value = 1
    return least_common_value

"""  """

oxygen_generator_rating = submarine_bits.copy()
CO2_scrubber_rating = submarine_bits.copy()

for column_index in range(len(oxygen_generator_rating.columns)):
    if len(oxygen_generator_rating) == 1:
        break
    value = get_least_common_value(oxygen_generator_rating, column_index)
    oxygen_generator_rating.drop(oxygen_generator_rating[oxygen_generator_rating[column_index] == value].index,
    inplace = True)

for column_index in range(len(CO2_scrubber_rating.columns)):
    if len(CO2_scrubber_rating) == 1:
        break
    value = get_most_common_value(CO2_scrubber_rating, column_index)
    CO2_scrubber_rating.drop(CO2_scrubber_rating[CO2_scrubber_rating[column_index] == value].index,
    inplace = True)


oxygen_generator_rating = "".join([str(oxygen_generator_rating.iloc[0, i])
for i in range(len(oxygen_generator_rating.columns))])

CO2_scrubber_rating = "".join([str(CO2_scrubber_rating.iloc[0, i])
for i in range(len(CO2_scrubber_rating.columns))])

print(f"oxygen generator rating= {oxygen_generator_rating}")
print(f"CO2 scrubber rating= {CO2_scrubber_rating}")

life_support_rating = int(oxygen_generator_rating, 2)*int(CO2_scrubber_rating, 2)

print(f"life support rating = {life_support_rating}")
