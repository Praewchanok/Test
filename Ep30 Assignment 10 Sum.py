sum = 0
# while sum!=100: # ผลรวมเท่ากับ 100
# while sum<=100:
while True:
    number=int(input("ตัวเลข : "))
    sum+=number # บวกเลขที่ป้อนแต่ละรอบ
    if sum>100:
        break
    print("ผลรวม = ",sum)
print("จบโปรแกรม")