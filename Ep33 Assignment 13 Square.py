# สร้างภาพวาด 4 เหลี่ยมจัตุรัส

number=int(input("Size : "))

for row in range(number):
    for column in range(number):
        print("X",end="")
    print(" ")