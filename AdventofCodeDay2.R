# load packages
library(googlesheets4)
library(dplyr)
# read submarine movement data into list 'submarine_movement' from google sheets
submarine_movement <- range_read("https://docs.google.com/spreadsheets/d/1YUBHAw4HpHMqiNiF4CG9QZzwXygiOZWdph2Jjda_Kj8/edit#gid=0", 
                                 col_types = NULL)

# create dataframe of 'submarine_movement' with columns 'direction' and 'magnitude' columns
submarine_movement <- as.data.frame(do.call(cbind, submarine_movement))

submarine_movement$magnitude <- as.integer(submarine_movement$magnitude)

horizontal_position = 0
vertical_position = 0

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

final_answer = horizontal_position*vertical_position


