# for num in range(10):
#     print(num)

# for num in range(1,11):
#     print(num)    

# for num in range(0, 11, 2):
#     print(num)

# for num in range(1,100,5):
#     print(num)

# chilli_wishlist= ['igloo', 'chicken', 'toy']

# for item in range(len(chilli_wishlist)):
#      print(chilli_wishlist[item])

# for item in chilli_wishlist:
#      print("chilli wants", item)

# chilli_wishlist= [
#     ['igloo'],
#     ['donut toy', 'ball', 'crocodile'],
#     ['chicken', 'peanut'],
#     ['box','kong','mat']
# ]

# for category in chilli_wishlist:
#     for item in category:
# #         print(item)

# # guess=""
# # while guess !="a":
# #     guess= input("Guess a letter:  ")

# # counter= 10
# # while counter <=10:
# #     print(counter)
# #     counter = counter + 1    

# # #------------------ Loops -- Question 1------ Groceries ASK FOOR HELP
# print("====Izzy's Food Mart======")

# from array import array
# from ast import Num
# from multiprocessing.sharedctypes import Value
# import numbers
# from unicodedata import category


food= [
        ['baby spinage', 2.78],
        ['hot chocolate', 11.10],
        ['crackers', 4.20],
        ['bacon', 9.90],
        ['carrots', 2.24],
        ['orangies', 6.19],
    ]

print("====Izzy's Food Mart======")
for category in food:
    item_name = category[0]
number_item = int(input(f"{item_name}: "))
print(item_name)
price = category[1]  
print(price * number_item)
print(f" TOTAL ${price * number_item}")

print("====Izzy's Food Mart======")


# #------------------ Loops -- Question 2------ 

# word = input(f"please enter word: ")
# for letter in word:
#      print(letter)

# #------------------ page 1Loops -- Question 3

# User input pyrimd

# ===========Exercises Page 2 Question 1==============
# print('~~~TIMES TABLES~~~~')
# input_number = int(input(f" Enter a number "))
# print = counter * input_number


# # #for Loops
# name= "Jenny"


# for letter in name:
#      print(letter)
# # #While Loops

# name ="Asli"
# while name !="Jemmy":
#     print(f"hi, {name}")
#     name= input ("Enter a name:")


# counter = 0

# while counter < 5:
#     print ("Hello")
#     print("counter1 :" + counter) #0 , 1
#     #Never do infinate loop it is bad for the computer RAM
#     counter +=1 #counter = counter +1
#     print('counter2 :', counter) #1,2

# #pop(0) starts from the beginine
# #pop removes and returns items form the index, the last one

# # for loops question 3-------------------------

# total = 0
# random_numbers = [3,5,,9,1]
# #a = random_numbers.pop()
# while random_numbers !=[]:
#     #number_to_add = random_numbers.pop()
#     #total += number_to add
#     total += random_numbers.pop()
# print(total )


# total = 0
# random_numbers = [3,5,,9,1]
# counter=0
# print(counter)
# print(random_numbers[counter]) #3
# while c < len(random_numbers):
#     total+=random_numbers[counter]
#     counter+=1
