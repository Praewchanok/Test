'''
โครงสร้างควบคุม (control structure)
1.แบบลำดับ
2.แบบเลือก
3.แบบทำซ้ำ
'''

age=int(input("อายุ : "))

# print(type(age)) # int
# print(type(age==15)) # bool

'''
if boolean expression:
    statement
'''
'''
if จริง :
    ทำอะไร
else :
    ทำอะไร
'''

# if age>=15 and age<20:
     # print("วัยรุ่น")
# elif age>=20 and age<30:
    # print("วัยผู้ใหญ่")

if age>=15 and age<=19:
    print("วัยรุ่น")
elif age>=20 and age<=29:
    print("วัยผู้ใหญ่")
elif age>=30 and age<=79:
    print("วัยทำงาน")
elif age>=80:
    print("วัยชรา")
else :
    print("วัยเด็ก")
    
print("จบโปรแกรม")
