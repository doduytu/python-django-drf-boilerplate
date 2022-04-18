import string
from tokenize import String


print("bài 1: viết chương trình nhập 3 số dương a,b,c . kiểm tra xem 3 số này có tạo thành một tam giác")

a = float(input())
b = float(input())
c = float(input())

print("Du lieu vua nhap tuong ung 3 canh tam giac:  a = " + str(a) + ", b = " + str(b) + ", c = " + str(c))
if (a < b + c) and (a > b - c):
    print("a = " + str(a) + ", b = " + str(b) + ", c = " + str(c) + " La 3 canh cua 1 tam giac")
else:
    print("a = " + str(a) + ", b = " + str(b) + ", c = " + str(c) + " Khong phai la 3 canh cua 1 tam giac")