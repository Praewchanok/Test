# ตารางหมากฮอต

number=int(input("Size : "))

for row in range(number):
    for column in range(number):
        if (row+column)%2==0:
            print("X",end="")
        else :
            print("O",end="")
        # print("X",end="") if (row+column)%2 == 0 else print("O",end="")
    
    print(" ")