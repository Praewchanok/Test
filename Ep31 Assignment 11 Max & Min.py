# ค้นหาตัวเลข มากสุด / น้อยสุด

max,min = 0,10000

while True:
    number=int(input("ตัวเลข : "))
    if number<0 : # กระโดดออกจาก loop
        break
    if number>max:
        max=number
    if number<min:
        min=number
print("ค่าสูงสุด = ",max)
print("ค่าต่ำสุด = ",min)
print("จบโปรแกรม")