#NHAP DU LIEU
dai = float(input("Nhập chiều dài đáy hình khối chữ nhật (cm): "))
rong = float(input("Nhập chiều rộng đáy hình khối chữ nhật (cm): "))
cao = float(input("Nhập chiều cao hình khối chữ nhật (cm): "))
so_le = int(input("Số lượng số lẻ cần hiển thị: "))
#TINH TOAN 
dien_tich_day = dai * rong
the_tich = dai * rong * cao
#XUAT KET QUA
print(f"Diện tích đáy hình chữ nhật = {round(dien_tich_day, so_le)} cm\u00b2")
print(f"Thể tích hình khối = {round(the_tich, so_le)} cm\u00b3")