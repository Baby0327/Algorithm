a, b, c, x, y = map(int, input().split())
print(min(c * min(x, y) * 2 + a * (x - min(x, y)) + b * (y - min(x, y)), x * a + y * b, c * max(x, y) * 2))