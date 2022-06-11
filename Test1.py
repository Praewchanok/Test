number=int(input("Number : "))
for i in range(1,number+1):
    
    if i %3 == 0 and i %5 == 0:
        print(i,"FizzBuzz")
    elif i %3 == 0:
        print(i,"Fizz")
    elif i %5 == 0:
        print(i,"Buzz")
    else :
        print(i)

print("จบโปรแกรม")