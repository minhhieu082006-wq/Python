from datetime import datetime, timedelta

# ================== i. THÔNG TIN HIỆN TẠI ==================
now = datetime.now()

print("===== i. THÔNG TIN HIỆN TẠI =====")
print("Năm hiện tại:", now.year)
print("Tháng hiện tại (bằng chữ):", now.strftime("%B"))
print("Tuần thứ mấy trong năm:", now.isocalendar()[1])
print("Tuần thứ mấy trong tháng:", (now.day - 1)//7 + 1)
print("Ngày thứ mấy trong năm:", now.timetuple().tm_yday)
print("Ngày dương lịch:", now.day)
print("Thứ:", now.strftime("%A"))
print("Giờ phút giây:", now.strftime("%H:%M:%S"))

# ================== ii. TÍNH SỐ NGÀY ==================
print("\n===== ii. TÍNH SỐ NGÀY =====")
d1 = "01/01/2020"
d2 = "05/01/2020"

date1 = datetime.strptime(d1, "%d/%m/%Y")
date2 = datetime.strptime(d2, "%d/%m/%Y")

print("Ngày 1:", d1)
print("Ngày 2:", d2)
print("Số ngày cách nhau:", abs((date2 - date1).days))

# ================== iii. CHUYỂN CHUỖI ==================
print("\n===== iii. CHUYỂN CHUỖI =====")
s = "Sep 18 2019 2:43PM"

date = datetime.strptime(s, "%b %d %Y %I:%M%p")

print("Chuỗi ban đầu:", s)
print("Sau khi chuyển:", date)

# ================== iv. CỘNG 5 GIÂY ==================
print("\n===== iv. CỘNG 5 GIÂY =====")
new_time = now + timedelta(seconds=5)

print("Hiện tại:", now.strftime("%H:%M:%S"))
print("Sau 5 giây:", new_time.strftime("%H:%M:%S"))