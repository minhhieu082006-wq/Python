# Nhập dữ liệu đầu vào (để dạng chuỗi để dễ duyệt từng chữ số)
n_str = input("Nhập số nguyên dương n: ")

# Khởi tạo các biến lưu trữ
chan = 0
le = 0
tong = 0
tich = 1
so_lon_nhat = '0'
la_may_man = True

# Duyệt qua từng chữ số trong chuỗi n_str
for chu_so in n_str:
    so = int(chu_so)
    
    # --- Bài 4: Đếm số lượng chữ số chẵn, số chữ số lẻ ---
    if so % 2 == 0:
        chan += 1
    else:
        le += 1
        
    # --- Bài 5: Tính tổng và tích các chữ số ---
    tong += so
    tich *= so
    
    # --- Bài 6: Tìm chữ số lớn nhất ---
    if chu_so > so_lon_nhat:
        so_lon_nhat = chu_so
        
    # --- Bài 7: Kiểm tra số may mắn (chỉ chứa 6 hoặc 8) ---
    if chu_so not in ['6', '8']:
        la_may_man = False

# --- XUẤT KẾT QUẢ ---
print("-" * 30)
print(f"Bài 4: Số lượng số lẻ: {le}, số lượng số chẵn: {chan}")
print(f"Bài 5: Tổng = {tong}, Tích = {tich}")
print(f"Bài 6: Số lớn nhất = {so_lon_nhat}")

if la_may_man:
    print(f"Bài 7: {n_str} là số may mắn.")
else:
    print(f"Bài 7: {n_str} KHÔNG phải số may mắn.")