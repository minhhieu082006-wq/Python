n = input("Nhập n: ")

S = 0

# lấy tất cả số con
for i in range(len(n)):
    for j in range(i + 1, len(n) + 1):
        so_con = int(n[i:j])
        S += so_con ** 2

print("Tổng S =", S)