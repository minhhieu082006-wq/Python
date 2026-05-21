triangle = lambda a, b, c: (
    "Không phải tam giác"
    if a + b <= c or a + c <= b or b + c <= a
    else "Tam giác đều" if a == b == c
    else "Tam giác cân" if a == b or b == c or a == c
    else "Tam giác vuông" if a*a + b*b == c*c or a*a + c*c == b*b or b*b + c*c == a*a
    else "Tam giác thường"
)

print(triangle(3, 4, 5))