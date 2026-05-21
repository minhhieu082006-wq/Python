import re

# Chuỗi S
S = """Chiều chiều trước bến Văn Lâu
Ai ngồi, ai câu, ai sầu, ai thảm
Ai thương, ai cảm, ai nhớ, ai trông
Thuyền ai thấp thoáng ven sông
Đưa câu mái vẩy chạnh lòng nước non"""

# Nhập từ cần đếm
word = input("Nhập từ cần đếm: ")

# KHÔNG chuyển về lower nữa

# Tìm đúng từ (phân biệt hoa thường)
matches = re.findall(r'\b' + re.escape(word) + r'\b', S)

# Đếm
count = len(matches)

print(f"Số từ '{word}' là: {count}")