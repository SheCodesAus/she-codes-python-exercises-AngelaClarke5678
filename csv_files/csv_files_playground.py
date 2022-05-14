import csv
from encodings import utf_8

with open("csv_files/2016_pilbara.csv") as file:
    file_reader = csv.reader(file, delimiter=",") #created an object
    for row in file_reader:
        print(row)

print("add a population")
population = []

with open("csv_files/2016_pilbara.csv", encoding="utf_8") as csv_file:
    reader = csv.reader(csv_file) #.reader is the external library that we imported, this function takes in the file. Reader is an Object
    for row in reader: #we cant just read the file we need to iterate over it to read it, seperates the list of rows that are being iterated 
        population.append(row)
print("Population of pilbara")
print(population)
print()
print(f"there are {len(population)} rows in the file")

print("age groups")
for age_group in population:
    print(f"{age_group[0]}: {age_group[1]}")

print("writing to CSV file")
# writing to CSV file
with open("csv_files/population.csv", mode = "w", encoding="utf_8") as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=",") #writer is the external library that we imported, this function takes in the file. writer is an Object

    for age_group in population: #age group 0 - 4 --> 4711 
        csv_writer.writerow([age_group[1], age_group[0]]) #4711, 0-4yrs


#find the mim value
numbers = [4,7,10,1,2]
min_value = numbers[0]
max_value = 0
index = 0

for num in numbers:
    if num < min_value:
        min_value = num
        index += 1
        print(f"min value: {num} index: {index}")
    if num > max_value:
        max_value = num
        print(f"max value: {num} index: {index}")

