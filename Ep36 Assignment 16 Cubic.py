# เกมทายเลขลูกเต๋า
# 1,2,3,4,5,6

import random

myrandom=random.randrange(1,7) # 1-6
k=1
correct=False

while True:
    number=int(input("Your Number = "))
    
    correct=(number==myrandom) # true / false
    
    if not correct:
        if (number<myrandom):
            print("+")
        if (number>myrandom):
            print("-")
    if correct:
        print("+ 1000 point")
        break
    # else :
        # print("-500 point")
    if number<0 or k==3:
        break
    k+=1
if not correct:
    print("-500 point")
print("Result = ",myrandom)
print("End Game")