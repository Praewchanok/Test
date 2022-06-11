weight=int(input("น้ำหนัก (kg) : "))
high=int(input("ส่วนสูง (cm) : "))/100

bmi=weight/(high**2)

if bmi>=0 and bmi<18.0:
    result="ต่ำกว่าเกณฑ์"
elif bmi>=18.5 and bmi<=22.9:
    result="มาตรฐาน"
elif bmi>=23.0 and bmi<=24.9:
    result="น้ำหนักเกิน"
elif bmi>=25.0 and bmi<=29.9:
    result="โรคอ้วนระดับ 1"
else :
    result="ไม่ทราบค่าชัดเจน"
print("BMI = ",bmi,"ทำนายว่า",result)