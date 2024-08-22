import random
import math 

lowerb=int (input("enter lowerbound value "))
upperb=int (input("enter upperbound value"))
#lowerb=int(lower)
#upperb=int(upper)
x=random.randint(lowerb,upperb)
availableguess=math.ceil(math.log( upperb - lowerb + 1,2))
print("please enter number you have ,",availableguess,"chances" )
flag = False
count=0

while count<availableguess:
    count=count+1
    guessnumber=int(input("enter your guess"))
    if x==guessnumber:
        print("congratuklation you are won ")
        flag = True
        break

    elif x>guessnumber:
        print("the entered number is very small")
    elif x<guessnumber:
        print("the entered number is very big")
if not False:
    print("the number is ",x,"better luck next time")
    
    