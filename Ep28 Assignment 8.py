# Break หยุดการทำซ้ำ / Continue กระโดดข้ามการทำงาน

'''
i=1
while i<=10 :
    print("รอบที่ = ",i)
    # if(i==5) :
        # break
    i+=1
print("จบโปรแกรม")

i=0
while i<=10 :
    i+=1
    # if (i==5) :
    if (i%2 !=0) : # i%2 == 0
        continue
    print("รอบที่ = ",i)
print("จบโปรแกรม")
'''
for i in range(1,11):
    # if (i%2 == 0) :
        # continue
    if (i==5):
        break
    print(i)
print("จบโปรแกรม")

