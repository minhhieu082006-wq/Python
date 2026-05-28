import math

# HÀM KIỂM TRA NGUYÊN TỐ 
def la_so_nguyen_to(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False

    return True

#  HÀM ĐẢO STROBOGRAMMATIC 
def dao_strobogrammatic(n):
    doi = {
        '0': '0',
        '1': '1',
        '6': '9',
        '8': '8',
        '9': '6'
    }

    s = str(n)
    ketqua = ""

    for ch in reversed(s):
        if ch not in doi:
            return -1
        ketqua += doi[ch]

    return int(ketqua)

#  KIỂM TRA STROBOGRAMMATIC 
def la_strobogrammatic(n):
    return dao_strobogrammatic(n) == n

# STROBOGRAMMATIC MỞ RỘNG 
# Chỉ cần đảo strobogrammatic hợp lệ
def la_strobogrammatic_morong(n):
    return dao_strobogrammatic(n) != -1

# a. In các số strobogrammatic nhỏ hơn 1 triệu
print("a. Cac so strobogrammatic < 1000000:\n")

for i in range(1000000):
    if la_strobogrammatic(i):
        print(i, end=" ")

print("\n\n")

# b. In các số nguyên tố strobogrammatic nhỏ hơn 1 triệu
print("b. Cac so nguyen to strobogrammatic < 1000000:\n")

for i in range(1000000):
    if la_strobogrammatic(i) and la_so_nguyen_to(i):
        print(i, end=" ")

print("\n\n")

# c. In các số strobogrammatic mở rộng nhỏ hơn 1 triệu
print("c. Cac so strobogrammatic mo rong < 1000000:\n")

for i in range(1000000):
    if la_strobogrammatic_morong(i):
        print(i, end=" ")

print("\n\n")

# d. In các số nguyên tố strobogrammatic mở rộng < 1 triệu
print("d. Cac so nguyen to strobogrammatic mo rong < 1000000:\n")

for i in range(1000000):
    if la_strobogrammatic_morong(i) and la_so_nguyen_to(i):
        print(i, end=" ")

print("\n\n")

# e. In các số không phải strobogrammatic, không phải số nguyên tố
# nhưng strobogrammatic của nó là số nguyên tố
print("e. Cac so khong phai strobogrammatic, khong phai so nguyen to")
print("   nhung dao strobogrammatic cua no la so nguyen to:\n")

for i in range(1000000):

    dao = dao_strobogrammatic(i)

    if dao != -1:

        if (not la_strobogrammatic(i)) and \
           (not la_so_nguyen_to(i)) and \
           la_so_nguyen_to(dao):

            print(i, "->", dao)