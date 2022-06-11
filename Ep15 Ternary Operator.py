# Ternary Operator
# "เงื่อนไขเป็นจริง" if expression else "เงื่อนไขอื่นๆ"

'''
if age>=15:
    print("วัยรุ่น")
else :
    print("วัยเด็ก")
    
print("จบโปรแกรม")
'''

age=int(input("อายุ : "))
print("วัยรุ่น") if age>=15 else print("วัยเด็ก")
print("จบโปรแกรม")