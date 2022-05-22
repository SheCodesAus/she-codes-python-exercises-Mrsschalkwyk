import os
import csv
cwd = os.getcwd()  # Get the current working directory (cwd)

print("This is my directory" + cwd)
files = os.listdir(cwd)  # Get all the files in that directory
print("These are the files ",files)
print("Files in %r: %s" % (cwd, files))

with open("2016_pilbara.csv") as csv_file:
    reader = csv.reader(csv_file)
    for line in reader:
        print(line)

population = []

with open("2016_pilbara.csv", encoding="utf-8") as csv_file:
    reader = csv.reader(csv_file) # create a reader or writer object
    for row in reader: #for each row create an empty list
        #seperates elements based on the delimiter that has been given

    for age_group in population: #age_group = ['0-4 years', '4711']
        print(f"{age_group[0]} {age_group[1]}")

# writing a csv file 
# with open("population.csv", mode="w", encoding="utf-8") as csv_file:
#     csv_writer = csv.writer(csv_file, delimiter=",")

#     for age_group in population: #age_group -> ['0-4 years', '4711']
#         csv_writer.writerow([age_group[1], age_group[0]]) #4711, 0-4 years
# #---Q4 --
# list_words = ['red, gree']
# A=0
# import csv
# with  open("csv")
# reader.

# for line in reader:
#     for item in line:
#         print("item")
# #use a boolean
# starts off as a false

# if item == list_words[0]:
#     REd_Total = A + 1
#     REd_Total =0 + 1
#     print(f'REd: {}Red_Total} ')
####+++ CLASS PROJECT
# numbers= [4,7,10,1,2] FIND THE LOWEST NUMBER IN LIST
# is this less < than in a list, assign it to a variable.
# assign the minimum to the first item. 

# numbers= [4,7,10,1,2]
# min_value = numbers[0]
# min_location=0
# index=0

# # capture the location on the minimun value
# #start at 0 incramind by 1 every round 
# for num in numbers:
#     if min_value> num:
#         min_value = num
#         min_value = index
#     index += 1
# print(min_value)        




