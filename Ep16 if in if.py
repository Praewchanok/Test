# if ซ้อน if
age=int(input("อายุ : "))

if age<=15:
    if age==15:
        print("มัธยมปีที่ 3")
    elif age==14:
        print("มัธยมปีที่ 2")
    elif age==13:
        print("มัธยมปีที่ 1")
    else :
        print("ประถมศึกษา")
else :
    print("มัธยมปลาย")
print("จบโปรแกรม")