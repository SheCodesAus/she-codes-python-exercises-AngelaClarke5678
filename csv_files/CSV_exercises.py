print("Q1 Write a program that reads incolours_20_simple.csvand output the colour data" )

import csv
from encodings import utf_8
import imp
from itertools import count

import math 

with open("csv_files/colours_20_simple.csv") as file:
    file_reader = csv.reader
    file_reader = csv.reader(file, delimiter=",") #created an object
    for row in file_reader:
        print(f"{row[0]} {row[1]} {row[2]}")

print("Q2 Write a program that reads in colours_20_simple.csv and outputs the colour data in order English, Hex then RGB" )

with open("csv_files/colours_20_simple.csv") as file:
    file_reader = csv.reader
    file_reader = csv.reader(file, delimiter=",")
    for row in file_reader:
        print(f"{row[2]}, Hex: {row[1]}, RGB: {row[0]}")

print("Q3 Write a program that reads in colours_20.csv and output the colour data in order English, Hex then RGB")
with open("csv_files/colours_20.csv") as file:
    file_reader = csv.reader
    file_reader = csv.reader(file,delimiter=",")
    for colour in file_reader:
        print(f"{colour[4]}, Hex: {colour[2]}, RGB: {colour[1]} ")

print("Q4. Using the same colour csv files,write a program that outputs the number of times each of the following colours appear in the English Name: red, green, blue, yellow")
with open("csv_files/colours_20.csv") as file:
        file_reader = csv.reader(file,delimiter=",")
        data = file. read()
        colour = "yellow"
        occurrences = data. count(colour)
        print(f"Number of occurrences of the word {colour}: ", occurrences)

print("Q4. Alternate way")

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

print("Q5. galaxies.py contains data about 82 different galaxies and their velocities(km/sec). Using this data, output the galaxy with the slowest velocity, and the galaxy with the highest velocity.")

with open("csv_files/galaxies.csv") as file:
    file_reader = csv.reader(file, delimiter=",")
    line_count = 0

    galaxy_max = 0
    value_max = -math.inf
    galaxy_min = 0

    for row in file_reader:
        if line_count == 0:
            print(f'column names are {",".join(row)}')
            line_count += 1
        else: 
            print(f'Our Galaxy is {row[0]} and the velocity is {row[1]}')
            line_count += 1
            if float(row[1]) > value_max:
                galaxy_max, value_max = row[0],float(row[1])

    for row in file_reader:
        if line_count == 0:
            print(f'column names are {",".join(row)}')
            line_count += 1
        else: 
            print(f'Our Galaxy is {row[0]} and the velocity is {row[1]}')
            line_count += 1
            if float(row[1]) > value_max:
                galaxy_max, value_max = row[0],float(row[1])
    print(f'Galaxy {galaxy_max} has the max velocity of {value_max}km/sec')
