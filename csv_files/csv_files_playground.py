import os
import csv
import os

# population =[]

# with open("csv_files\pilbara.csv") as csv_file:
#     reader = csv.reader(csv_file)
#     for line in reader:
#      print(line)
#     population.append(line)
# print(population)

# for age_group in population: #age_group=
#     print(f"[age_group[0],age_group[1]]")

# #writing to a csv file
# with open("population.csv", mode="w", encoding="utf-8") as csv_file:
#     csv_writer = csv.writer(csv_file, deliminter=",")
    
    # for age_group in population:
    #     csv_writer.writerow([age_group[1], age_group[0]])
# ==============QUESTION ONE++++++++++++



outputs = []
with open("csv_files\colours_20.csv", encoding="utf-8") as csv_file:
     reader = csv.reader(csv_file)

     table:list[dict[str,float]]=[]
     for line in reader:
         outputs.append(line)
print(outputs)



