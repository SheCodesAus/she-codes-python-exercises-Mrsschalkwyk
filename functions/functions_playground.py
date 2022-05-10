# # from turtle import done


# # print
# # input #build in functions

# # #calling a function, you dont need to define;
# # #definition:
# # #z = f(x,y)

# # def hello(): #this is now a funtcion not a veriable
# #     print('hello')#this is the bosy of a funtion
# # hello(): this is calling the function



# # how to capture the function and put it into a variable
# # use a return
# # RETURN: after return you get the same? & then that function is done

# from tkinter import Variable


# def add(number1,nummber2): #formal parameters are number1 & number2
#     result = number1 + nummber2
#     #number1 & number two are local variables
#     return result 
# print(add(5,3)) #number1=5 , number2=3 has been assigned
#  #print()= result
#  assign Variable

#  sum = add()

def create_greeting(name):
    greeting = f"Hello, {name}!"
    retun greeting

print(create_greeting("chilli"))    

def tripple(number):
    results = 3 * number
    print(results)
    # return 3 * number #how to #x3=print

def convert_cm_to_in(length_cm):
    length_in_inches = length_cm / 2.54
    return length_in_inches
print(convert_cm_to_in)    

def calculate_mean(x,y):
    total = x + y
    mean = total / 2
    return mean

#function can be no or as many 
# if you want to make a function and save it or later write PASS under it to skip
#     

def convert_fh_to_c(temp):
    formula = temp
#google formula

# 

generate_summery(a)
