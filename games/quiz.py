from multiprocessing.connection import answer_challenge


print("welcome to my quiz ")

playing= input( "do you want to play? ")

if playing.lower() =="yes":
    
    print("Okay! Lets play")
else:
    print('bye')
score = 0 

answer = input("what does cpu stand for? ")
if answer == "central processing unit":
    print('Correct ')
    score += 1

else: 
    print("Incorrect")


answer = input("how do you spell 1? ")
if answer == "one":
    print('Correct ')
    score += 1

else: 
    print("Incorrect")  


answer = input("how do you spell 2? ")
if answer == "two":
    print('Correct ')
    score += 1

else: 
    print("Incorrect")    

answer = input("how do you spell 3? ")
if answer == "three":
    print('Correct ')
    score += 1

else: 
    print("Incorrect")        


print("YOu got " + str(score) + "questions correct! ")
print("YOu got " + str(score / 4) * 100 "%")