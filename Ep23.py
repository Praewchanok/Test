'''
# 1 การเข้าถึงตัวอักษร string
name=" Thanchanok Tessakarn " # index => 0 นับช่องว่างด้วย
print(name[0:14]) # ก่อนถึงจุดสุดท้าย Thanchanok Tes
print(name[-4)

# 2 หาจำนวนตัวอักษร (len function)
print(len(name))

# 3 การลบช่องว่างซ้ายขวา (strip)
name=name.strip()
name=name.lstrip() # การลบช่องว่างด้านซ้าย (strip)
name=name.rstrip() # การลบช่องว่างด้านขวา (strip)

# 4 แปลง case ของ string
name="praew praew"
print(name.upper()) # พิมพ์ใหญ่ทั้งหมด
print(name.lower()) # พิมพ์เล็กทั้งหมด
print(name.capitalize()) # พิมพ์ใหญ่ตัวแรก

# 5 การแทนที่
print(name.replace("praew","pisces"))
print(name.replace("praew","pisces",1)) # เปลี่ยนเฉพาะตำแหน่ง

# 6 การเช็คข้อความ => true , false
x = "praew" in name
print(x)
if x:
    name=name.replace("praew","p r a e w = ",1)
print(name)

# 7 การต่อ string (Concatinate) +
from cgitb import text


fname="Thanchanok"
lname="Tessakarn"
age="25"
salary=15000.5
fullname=fname+lname+age
print(fullname)
print("ชื่อ : "+fname+"\tนามสกุล : "+lname+"\nอายุ : "+age)
print("ชื่อ : "+fname+"\nนามสกุล : "+lname+"\nอายุ : "+age)

# 8 การจัดรูปแบบการแสดงผล {}
text="ชื่อ : {}\tนามสกุล : {}\tอายุ : {}"
text="ชื่อ : {}\tนามสกุล : {}\tอายุ : {}\tอาชีพ : {}\tเงินเดือน : {:.2f}" # ระบุตำแหน่งได้ , .2f => ทศนิยม 2 ตำแหน่ง
print(text.format(fname,lname,age,"Programer",salary))

# 9 การนับจำนวนคำในประโยค
fruit="ไปซื้อผลไม้ มีทุเรียน มังคุด ข้ามเหนียวทุเรียน ที่ตลาด จะแวะไปสวนทุเรียนด้วย"
print(fruit.count("ทุเรียน"))
'''
# 10 เช็คคำขึ้นต้น => true , false
name="นาย สหภาพ วงษ์ราษฎร์ "
# print(name.startswith("นาย"))
if name.startswith("นาย"):
    print("เพศชาย")
else :
    print("อื่นๆ")

lottery="020880"
if lottery.endswith("0"):
    print("WIN")
else :
    print("LOSE")