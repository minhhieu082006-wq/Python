import math

la_chinh_phuong = lambda n: n >= 0 and int(math.sqrt(n)) ** 2 == n

la_tam_giac = lambda a, b, c: (
    a > 0 and b > 0 and c > 0 and
    a + b > c and
    a + c > b and
    b + c > a
)

la_tam_giac_vuong = lambda a, b, c: (
    a**2 + b**2 == c**2 or
    a**2 + c**2 == b**2 or
    b**2 + c**2 == a**2
)

n = int(input("Nhap so nguyen n: "))

if la_chinh_phuong(n):
    print(f"{n} la so chinh phuong")
else:
    print(f"{n} khong phai la so chinh phuong")

print("\nNhap 3 canh tam giac:")
a = float(input("Nhap canh a: "))
b = float(input("Nhap canh b: "))
c = float(input("Nhap canh c: "))

if la_tam_giac(a, b, c):
    print("Ba canh tao thanh tam giac")

    if a == b == c:
        print("Day la tam giac deu")

    elif a == b or a == c or b == c:
        if la_tam_giac_vuong(a, b, c):
            print("Day la tam giac vuong can")
        else:
            print("Day la tam giac can")

    elif la_tam_giac_vuong(a, b, c):
        print("Day la tam giac vuong")

    else:
        print("Day la tam giac thuong")

else:
    print("Ba canh khong tao thanh tam giac")