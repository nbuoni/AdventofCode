# import packages

import pandas as pd

# import submarine diagnostic report as pandas dataframe with one digit of bit per cell
submarine_bits = pd.read_csv(r'/Users/ninabuoni/Documents/AdventofCode/AdventofCodeDay3Data.csv',
                             header = None,
                             index_col = False)

# define function to obtain most common column value of data frame containing bits given data frame and column index
def get_most_common_value(df, column_index):
    ratio = df[column_index].sum()/len(df)
    if ratio >= 0.5000:
        most_common_value = 1
    else:
        most_common_value = 0
    return most_common_value

# define function to obtain least common column value of data frame containing bits given data frame and column index
def get_least_common_value(df, column_index):
    ratio = df[column_index].sum()/len(submarine_bits)
    if ratio >= 0.5000:
        least_common_value = 0
    else:
        least_common_value = 1
    return least_common_value

""" To find the oxygen generator rating determine the most common value in the current
bit position starting with the first bit and continuining with subsequent bits.
Keep only numbers with that bit in the corresponding position. To find the CO2
scrubber rating, determine the least common value in the current bit position
starting with the first bit and continuining with subsequent bits. Keep only
numbers with that bit in the corresponding position. The process ends when only
one number remains. The remaining number is the desired rating. """

oxygen_generator_rating = submarine_bits.copy()
CO2_scrubber_rating = submarine_bits.copy()

for column_index in range(len(oxygen_generator_rating.columns)):
    if len(oxygen_generator_rating) == 1:
        break
    value = get_most_common_value(oxygen_generator_rating, column_index)
    oxygen_generator_rating.drop(oxygen_generator_rating[oxygen_generator_rating[column_index] != value].index,
    inplace = True)

for column_index in range(len(CO2_scrubber_rating.columns)):
    if len(CO2_scrubber_rating) == 1:
        break
    value = get_most_common_value(CO2_scrubber_rating, column_index)
    CO2_scrubber_rating.drop(CO2_scrubber_rating[CO2_scrubber_rating[column_index] == value].index,
    inplace = True)

# construct oxygen generator rating and CO2 scrubber rating
oxygen_generator_rating = "".join([str(oxygen_generator_rating.iloc[0, i])
for i in range(len(oxygen_generator_rating.columns))])

CO2_scrubber_rating = "".join([str(CO2_scrubber_rating.iloc[0, i])
for i in range(len(CO2_scrubber_rating.columns))])

# print oxygen generator rating and CO2 scrubber rating
print(f"oxygen generator rating= {oxygen_generator_rating}")
print(f"CO2 scrubber rating= {CO2_scrubber_rating}")

# calculate life support rating in decimal format
life_support_rating = int(oxygen_generator_rating, 2)*int(CO2_scrubber_rating, 2)

# print life support rating
print(f"life support rating = {life_support_rating}")
