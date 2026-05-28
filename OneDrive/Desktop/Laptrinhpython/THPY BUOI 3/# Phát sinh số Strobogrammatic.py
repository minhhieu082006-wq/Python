# Phát sinh số Strobogrammatic
# n từ 2 -> 10

def sinh_strobogrammatic(n, tong_do_dai):

    if n == 0:
        return [""]

    if n == 1:
        return ["0", "1", "8"]

    ds = sinh_strobogrammatic(n - 2, tong_do_dai)

    ketqua = []

    for s in ds:

        # Không cho số bắt đầu bằng 0
        if n != tong_do_dai:
            ketqua.append("0" + s + "0")

        ketqua.append("1" + s + "1")
        ketqua.append("6" + s + "9")
        ketqua.append("8" + s + "8")
        ketqua.append("9" + s + "6")

    return ketqua


# ================== MAIN ==================

n = int(input("Nhap n (2 <= n <= 10): "))

while n < 2 or n > 10:
    n = int(input("Nhap lai n: "))

# -------------------------------------------------
# a. Tất cả số strobogrammatic gồm n chữ số
# -------------------------------------------------
print("\na. Cac so strobogrammatic gom", n, "chu so:\n")

ds1 = sinh_strobogrammatic(n, n)

for so in ds1:
    print(so, end=" ")

# -------------------------------------------------
# b. Tất cả số strobogrammatic mở rộng gồm n chữ số
# -------------------------------------------------
# Mở rộng: cho phép thêm 2 và 5 đứng giữa
# (theo kiểu đề trước)

print("\n\nb. Cac so strobogrammatic mo rong gom", n, "chu so:\n")

ds2 = ds1.copy()

# thêm các số có 2 và 5 ở giữa nếu n lẻ
if n % 2 == 1:

    ds_morong = []

    for s in sinh_strobogrammatic(n - 1, n - 1):

        giua = len(s) // 2

        ds_morong.append(s[:giua] + "2" + s[giua:])
        ds_morong.append(s[:giua] + "5" + s[giua:])

    ds2.extend(ds_morong)

# xóa trùng và sắp xếp
ds2 = sorted(set(ds2))

for so in ds2:
    print(so, end=" ")