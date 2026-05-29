la_so_chinh_phuong = lambda n: int(n ** 0.5) ** 2 == n


la_so_hoan_thien = lambda n: sum(i for i in range(1, n) if n % i == 0) == n


print("===== CAC SO CHINH PHUONG TU 1 DEN 10000 =====")

for i in range(1, 10001):
    if la_so_chinh_phuong(i):
        print(i, end=" ")

print("\n")

print("===== CAC SO HOAN THIEN TU 1 DEN 10000 =====")

for i in range(1, 10001):
    if la_so_hoan_thien(i):
        print(i, end=" ")

print()