
import csv
from encodings import utf_8

list_words = ["red", "green", "blue", "yellow"]
red_total = 0
green_total = 0
blue_total = 0
yellow_total = 0

with open("csv_files/colours_20.csv") as file:
    file_reader = csv.reader(file,delimiter=",")
    # next(file_reader) #skips header
    for line in file_reader:
        if list_words[0] in line[4]:
                red_total += 1
        elif list_words[1] in line[4]:
                green_total += 1   
        elif list_words[2] in line[4]:
                blue_total += 1   
        elif list_words[3] in line[4]:
                yellow_total += 1    
    print(f"Red: {red_total} Green: {green_total} Blue: {blue_total} Yellow: {yellow_total}")

#find the mim value
numbers = [4,7,10,1,2]
min_value = numbers[0]
max_value = 0
min_location = 0
index = 0

for num in numbers:
        if num < min_value:
                min_value = num
                min_location = index
index += 1
print(f"min value: {num} index: {index}")

        if max_value < num:
                max_value = num
                index += 1
print(f"max value: {num} index: {index}")
