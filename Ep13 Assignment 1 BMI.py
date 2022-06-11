# โปรแกรมคำนวณค่า BMI (ดัชนีมวลกาย)
# BMI = น้ำหนัก (kg) / ส่วนสูง * ส่วนสูง (m)

# input / convert to integer
weignt=int(input("น้ำหนัก (kg) : "))
high=int(input("ส่วนสูง (cm) : "))/100

# process
# high/=100 # high=high/100 # cm => m
# bmi=weignt/(high*high) # calculate bmi
# bmi=weignt/high**2

# output
print("BMI : ", weignt/high**2)