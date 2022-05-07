import csv
from encodings import utf_8

with open("csv_files/2016_pilbara.csv") as file:
    file_reader = csv.reader(file, delimiter=",") #created an object
    for row in file_reader:
        print(row)

print("add a population")
population = []

with open("csv_files/2016_pilbara.csv", encoding="utf_8") as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
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
    csv_writer = csv.writer(csv_file, delimiter=",")

    for age_group in population: #age group 0 - 4 --> 4711 
        csv_writer.writerow([age_group[1], age_group[0]]) #4711, 0-4yrs

        