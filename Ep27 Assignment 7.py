# แบบสูตรคูณ

start=int(input("แม่สูตรคูณเริ่มต้น = "))
stop=int(input("แม่สูตรคูณสุดท้าย = "))
for x in range(start,stop+1) :
    print("สูตรคูณแม่ ",x)
    for y in range(1,12) :
        print(x,"x",y,"=",(x*y))