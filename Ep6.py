# Type Coversion
from unittest import result


x = 10
y = 3.14
z = "20" # str

print(type(x))
print(type(y))
print(type(z))

# บวกเลข
result = x+y # 10 + 3.14 = 13.14
print(result)

# string => int
result2 = x+int(z) # 10+20 = 30
print(result2)

# int => string
result3 = str(x)+z # "10"+"20" = "1020"
print(result3)

# float => string
print(str(y))

z=float(z) # float
print(type(z))