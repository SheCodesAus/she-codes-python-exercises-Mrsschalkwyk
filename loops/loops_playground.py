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
#     print(chilli_wishlist[item])

# for item in chilli_wishlist:
#     print("chilli wants", item)

# chilli_wishlist= [
#     ['igloo'],
#     ['donut toy', 'ball', 'crocodile'],
#     ['chicken', 'peanut'],
#     ['box','kong','mat']
# ]

# for category in chilli_wishlist:
#     for item in category:
#         print(item)

# guess=""
# while guess !="a":
#     guess= input("Guess a letter:  ")

# counter= 10
# while counter <=10:
#     print(counter)
#     counter = counter + 1    

#------------------ Loops -- Question 3

#for Loops
name= "Jenny"


for letter in name:
    print(letter)
#While Loops

name ="Asli"
while name !="Jemmy":
    print(f"hi, {name}")
    name= input ("Enter a name:")


counter = 0

while counter < 5:
    print ("Hello")
    print("counter1 :" + counter) #0 , 1
    #Never do infinate loop it is bad for the computer RAM
    counter +=1 #counter = counter +1
    print('counter2 :', counter) #1,2

#pop(0) starts from the beginine
#pop removes and returns items form the index, the last one

# for loops question 3-------------------------

total = 0
random_numbers = [3,5,,9,1]
#a = random_numbers.pop()
while random_numbers !=[]:
    #number_to_add = random_numbers.pop()
    #total += number_to add
    total += random_numbers.pop()
print(total )


total = 0
random_numbers = [3,5,,9,1]
counter=0
print(counter)
print(random_numbers[counter]) #3
while c < len(random_numbers):
    total+=random_numbers[counter]
    counter+=1