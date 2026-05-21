# Hàm kiểm tra số nguyên tố
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Khởi tạo danh sách
numbers = []

# Nhập dữ liệu nhiều lần
while True:
    try:
        n = int(input("Nhập số nguyên: "))
        numbers.append(n)
    except:
        print("Nhập sai, vui lòng nhập số nguyên!")
        continue
    
    choice = input("Bạn có muốn nhập tiếp không? (Y/N): ").strip().lower()
    if choice == 'n':
        break

# a) In các số nguyên tố
primes = [x for x in numbers if is_prime(x)]
print("Các số nguyên tố:", primes)

# b) Tính trung bình cộng số âm và số dương
negatives = [x for x in numbers if x < 0]
positives = [x for x in numbers if x > 0]

if negatives:
    avg_neg = sum(negatives) / len(negatives)
else:
    avg_neg = 0

if positives:
    avg_pos = sum(positives) / len(positives)
else:
    avg_pos = 0

print("Trung bình số âm:", avg_neg)
print("Trung bình số dương:", avg_pos)

# c) Số lớn nhất, nhỏ nhất
if numbers:
    print("Số lớn nhất:", max(numbers))
    print("Số nhỏ nhất:", min(numbers))

# d) Kiểm tra tăng dần
is_increasing = True
for i in range(len(numbers) - 1):
    if numbers[i] > numbers[i + 1]:
        is_increasing = False
        break

if is_increasing:
    print("Danh sách đã được sắp xếp tăng dần")
else:
    print("Danh sách chưa được sắp xếp tăng dần")