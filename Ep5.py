# กฎการตั้งชื่อ

"""
1.ตัวเลข ตัวอักษร เครื่องหมาย
2.ห้ามขึ้นต้นด้วยตัวเลขและสัญลักษณ์พิเศษ ยกเว้น _
3.ห้ามซ้ำกับ keyword
4.case sentitive (พิมพ์เล็ก พิมพ์ใหญ่)
"""

from tokenize import Name


a=10
x="Thank you"
_1="Thank you"

name="A"
NAME="B"
nAmE="C"

print(name)
print(NAME)
print(nAmE)
print(Name)