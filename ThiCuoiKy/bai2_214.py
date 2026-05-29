# Hàm kiểm tra số nguyên tố
def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
# Hàm đếm số nguyên tố nhỏ hơn n
def dem_so_nguyen_to_nho_hon(n):
    dem = 0
    for i in range(2, n):
        if la_so_nguyen_to(i):
            dem += 1
    return dem
# Hàm liệt kê các ước là số nguyên tố
def liet_ke_uoc_la_so_nguyen_to(n):
    ds_uoc_nguyen_to = []
    for i in range(1, n + 1):
        if n % i == 0 and la_so_nguyen_to(i):
            ds_uoc_nguyen_to.append(i)
    return ds_uoc_nguyen_to
# CHUONGTRINH
n = int(input("Nhập số nguyên dương n: "))
if n <= 0:
    print("Vui lòng nhập số nguyên dương!")
else:
    if la_so_nguyen_to(n):
        print(n, "là số nguyên tố")
    else:
        print(n, "không phải là số nguyên tố")
    print("Số lượng số nguyên tố nhỏ hơn", n, "là:", dem_so_nguyen_to_nho_hon(n))
    print("Các ước số của", n, "là số nguyên tố:", end=" ")
    ds = liet_ke_uoc_la_so_nguyen_to(n)
    if len(ds) == 0:
        print("Không có")
    else:
        for x in ds:
            print(x, end=" ")