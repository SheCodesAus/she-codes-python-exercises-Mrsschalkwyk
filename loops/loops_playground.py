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


# food= [
#         ['baby spinage', 2.78],
#         ['hot chocolate', 3.70],
#         ['crackers', 2.10],
#         ['bacon', 9.00],
#         ['carrots', 0.56],
#         ['orangies', 3.08],
#     ]
# total = 0
# total_list= []
# for category in food:
#     item_name = category[0]
#     number_item = int(input(f"{item_name}: "))
#     # print(item_name)
#     price = category[1]  
#     # print(price * number_item)
#     total_per_item = price * number_item
#     total += total_per_item
#     total_list.append([item_name,total_per_item])
# print(total_list)

# # print(f" TOTAL ${price * number_item}")
# print("====Izzy's Food Mart======")
# for item in total_list:
#     print(f"{item[0]} ${item[1]}")
# print("=============")
# print(total)

# #------------------ Loops -CATSsdG- Question 2------ 
# #loop length
# print(range (4))
# word = input(f"please enter word: ")
# # for letter in word:
# #             print(letter)
# for number in range(len(word)):
            # print(number,word[number])
#Output a string of CATS

# letters= ['c','a','t','s']
# items  = (0,'c') #you can unpack veriables
# index, letter = items
# for index,letter in enumerate(letters):
#     #print(letter[0], letter[1])
#     print(index,letter)

# enumerate(itteration)=index = tuple



# #------------------ page 1Loops -- Question 3

# User input pyrimd
# input_number = int(input(f" Enter a number "))

# for number in range(input_number):
#     print((number+1) *"*")

#FUll pyrimd not mine
# print("Enter Number of Rows: ")
# row = int(input())
# print("Star Pyramid of " + str(row) + " Rows or Lines: ")
# for i in range(row):
#     for s in range(row, i, -1):
#         print(end=" ")
#     for j in range(i+1):
#         print(end="* ")
#     print()

# ===========Exercises Page 2 Question 1==============
# print('~~~TIMES TABLES~~~~')
# counter= +1
# input_number = int(input(f" Enter a number "))
# print = counter * input_number

#first attempt
# input_number = int(input(f" Enter a number"))
# output= range(len(input_number))
# for num in range(input_number):
#     print (output * input_number)
#second attempt
# input_number = int(input(f"please enter word: "))
# for num in input_number:
#             print(num)
# for number in range(len(input_number)):
#             print(number,input_number[number])

# #final
# def print_table(num): 
#     """ This function prints multiplication table of a given number"""
#     for i in range(1,11): 
#         print(num,' x ', i, ' = ',num*i) 
# # end of function table


# # input a number
# n = int(input("Please Enter a number to print its multiplication table:"))

# call the function tanle by passing actual parameter 'n' 

# print_table(n)
#========================================================
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
