import math

# Hàm tìm UCLN
def ucln(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Hàm đảo số
def dao_so(n):
    return int(str(n)[::-1])

a = int(input("Nhập a: "))
b = int(input("Nhập b: "))

dem = 0

print("Các số thân thiện là:")

for i in range(a, b + 1):
    dao = dao_so(i)

    if ucln(i, dao) == 1:
        print(i, end=" ")
        dem += 1

print("\nSố lượng:", dem)