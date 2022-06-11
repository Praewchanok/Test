# โครงสร้างควบคุมแบบทำซ้ำ
# while จำนวนรอบไม่ชัดเจน
# for จำนวนรอบชัดเจน
'''
while expression :
    statemant


i=1 # ตัวนับจำนวนรอบ
while i<=3: # 1<=3 , 2<=3 , 3<=3 , 4<=3 = false หยุดการทำงานเลย
    # print("Hello World")
    print("รอบที่ : ",i)
    i=i+1 # 2 , 3 , 4
print("จบโปรแกรม")

i=1 # ตัวนับจำนวนรอบ
summation = 0 # เก็บผลการบวกเลขตามจำนวนรอบ
average = 0 # ผลรวม / จำนวนรอบ
count=int(input("จำนวนรอบ : "))
# 1+2+3+4+5

while i<=count: 
    summation+=i # เก็บผลรวมของ i แต่ละรอบ 1+2+3
    print("รอบที่ = ",i,"SUM = ",summation)
    i+=1 # 1,2,3,4,5
average=summation/count
print("ผลรวม = ",summation)
print("ค่าเฉลี่ย = ",average)
'''

# for i in range(start,stop-1,step) กำหนดรอบ
 # summation=0
for i in range(10,0,-1): # เริ่มต้นที่ 0 = 3-1 => รอบ 0 รอบ 1 รอบ 2
    print("รอบที่ = ",i,) # รอบ 0 รอบ 1 รอบ 2
    # print("รอบที่ = ",i,"SUM = ",summation)
    # print("รอบที่ = ",i+1,"SUM = ",summation) # รอบ 1 รอบ 2 รอบ 3
    # summation+=i
# print("ผลรวม = ",summation)
