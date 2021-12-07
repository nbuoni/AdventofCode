# loads packages
library(googlesheets4)
library(dplyr)

# reads submarine movement data into list 'submarine_movement' from google sheets
submarine_movement <- range_read("https://docs.google.com/spreadsheets/d/1YUBHAw4HpHMqiNiF4CG9QZzwXygiOZWdph2Jjda_Kj8/edit#gid=0", 
                                 col_types = NULL)

# creates dataframe of 'submarine_movement' with columns 'direction' and 'magnitude' columns
submarine_movement <- as.data.frame(do.call(cbind, submarine_movement))

# changes data type of 'magnitude' column from character to int
submarine_movement$magnitude <- as.integer(submarine_movement$magnitude)

# sets horizontal and vertical position equal to 0
horizontal_position = 0
vertical_position = 0


#loops through submarine_movement to determine final horizontal and vertical
#position given that 'forward X' increases horizontal position by X units, 'down
#X' increases the depth by X units, and 'up X' decreases the depth by X units.


for (cell in 1:1000) {
  if (submarine_movement$direction[cell] == "forward") {
    horizontal_position = horizontal_position + submarine_movement$magnitude[cell]
  }
  else if (submarine_movement$direction[cell] == "up") {
    vertical_position = vertical_position - submarine_movement$magnitude[cell]
  }
  
  else {
    vertical_position = vertical_position + submarine_movement$magnitude[cell]
    }
}

# calculates final position by multiplying final horizontal position by final depth
final_position = horizontal_position*vertical_position


