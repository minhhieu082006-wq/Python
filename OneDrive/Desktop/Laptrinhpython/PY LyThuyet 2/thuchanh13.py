import re

def chuan_hoa_chuoi(text):
    lines = text.split('\n')
    result = []

    for line in lines:
        line = line.strip()
        line = re.sub(r'\s+', ' ', line)
        line = re.sub(r'\s+([.,])', r'\1', line)
        line = re.sub(r'([.,])([^\s])', r'\1 \2', line)
        result.append(line)

    return '\n'.join(result)


# ===== DỮ LIỆU MẪU =====
text = """    Quê  hương
Quê hương là  chùm khế  ngọt .
   Cho con trèo hái mỗi ngày .
Quê hương là đường đi học .
Con về rợp bướm vàng bay .
Đỗ  Trung  Quân    """

print("Kết quả:\n")
print(chuan_hoa_chuoi(text))