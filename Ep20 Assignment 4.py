# แลกเงินและหาจำนวนแบงค์

# 2000 => 1000 = 2 ใบ
# 1500 => 1000 = 1 ใบ, 500 = 1 ใบ
# 1800 => 1000 = 1 ใบ, 500 = 1 ใบ, 100 = 3 ใบ
# 100 => 50 = 2 ใบ

number=int(input("จำนวนเงิน : "))

if number>=1000:
    print("แบงค์ 1000 : ",number//1000,"ใบ")
    number%=1000 # number = number % 1000 
if number>=500:
    print("แบงค์ 500 : ",number//500,"ใบ")
    number%=500 # number = number % 500
if number>=100:
    print("แบงค์ 100 : ",number//100,"ใบ")
    number%=100 # number = number % 100
if number>=50:
    print("แบงค์ 50 : ",number//50,"ใบ")
    number%=50 # number = number % 50
if number>=20:
    print("แบงค์ 20 : ",number//20,"ใบ")
    number%=20 # number = number % 20