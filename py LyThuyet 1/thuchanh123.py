# ==========================================
# BÀI 1: Bỏ qua số chia hết cho 3 (dùng continue)
# ==========================================
print("--- Bài 1 ---")
a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b (a < b): "))

print(f"Kết quả Bài 1:", end=" ")
for i in range(a, b + 1):
    if i % 3 == 0:
        continue  # Bỏ qua các số chia hết cho 3
    print(i, end=" ")
print("\n") # Xuống dòng để phân cách bài


# ==========================================
# BÀI 2: Chuỗi số Fibonacci đến <= n
# ==========================================
print("--- Bài 2 ---")
n_fib = int(input("Nhập số nguyên n cho Fibonacci: "))

f1, f2 = 0, 1
print(f"Kết quả Bài 2:", end=" ")
while f1 <= n_fib:
    print(f1, end=" ")
    f1, f2 = f2, f1 + f2
print("\n")


# ==========================================
# BÀI 3: Số có các ký số giống nhau (từ 11 đến n)
# ==========================================
print("--- Bài 3 ---")
n_kk = int(input("Nhập số nguyên dương n (n >= 11): "))

print(f"Kết quả Bài 3:", end=" ")
for i in range(11, n_kk + 1):
    s = str(i)
    # Kiểm tra nếu tất cả các chữ số đều giống nhau
    if all(char == s[0] for char in s):
        print(i, end=" ")
print("\n")
