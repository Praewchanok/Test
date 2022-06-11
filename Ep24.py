# แปลงอุณหภูมิ
from unittest import result


temp=input("อุณหภูมิ (องศา) : ")
degree=int(temp[:-1]) # เลือกตั้งแต่ตัวแรกถึงตัวก่กอนสุดท้าย
unit=temp[-1].upper()


if unit=="C":
    result=(9*degree)/5+32 # C => F
    unit_resalt="ฟาเรนไฮน์"
if unit=="F":
    result=(degree-32)*5/9 # F => C
    unit_resalt="เซลเซียส"

print("แปลงอุณหภูมิ = ",temp.upper(),"เป็น",unit_resalt,"=",result)
