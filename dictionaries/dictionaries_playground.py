# students = {"Zohreh": 123, "Dani": 555}  
# #Keyvalue = zohreh
# #Key-value pairs
# #key are unique
# #keys need to be be immutable() cant be changed
# #dats type, string, int, float, not list cant be changed
# #unordered can be all over the place
# print(students)
# students["Donna"] = 189 #Can index using a string #this is how you add to the dictonary
# school={"asli yoruk": [12]}

# #delete = del students["Dani"]
# students["Dani"] = 999

# student_numbers = {"Zohreh": 123, "Dani": 555, "Asli":123}  

# for student_name, student_no in student_numbers.items():
#     print(student_name)

# for i in student_numbers.keys():
#     print(i) 
    
# for i in student_numbers.values():
#     print(i)    

groceries = {"Baby Spinach": 2.78,
"Hot Chocolate": 3.70,
"Crackers": 2.10,"Bacon": 9.00,
"Carrots": 0.56,
"Oranges": 3.08,
}

groceries["Hot Chocolate"] = 2.70 #change the price of crackers
del groceries["crackers"]

print(groceries)
# looking at a specific valueprint(groceries["Baby Spinach"])
# # adding a new itemgroceries["Avocadoes"] = 1.00print(groceries)