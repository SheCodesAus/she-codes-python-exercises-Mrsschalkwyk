import os
import csv
import os

population =[]

with open("csv_files/2016_pilbra.csv", encoding="utf-8") as csv_file
reader = csv.reader(csv_file)
for line in reader:
    population.append(line)
print(population)

for age_group in population: #age_group=
    print(f"[age_group[0],age_group[1]]")

with open("population.csv", mode="w" encoding="utf-8") as csv.file
    
