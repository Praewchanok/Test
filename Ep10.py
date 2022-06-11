# ตัวดำเนินการทางตรรกศาสตร์

#AND = และ
#OR = หรือ
#NOT = ไม่

# คำตอบ 2 คำตอบ => จริง / เท็จ

x = (10>5) # ค่า x = bool
y = (10==5) # ค่า y = bool
print(x)
print(y)

# z = x and y # z = (10>5) and (10==5)
z = x or y # z = (10>5) or (10==5)
print(z)
# print(not z)