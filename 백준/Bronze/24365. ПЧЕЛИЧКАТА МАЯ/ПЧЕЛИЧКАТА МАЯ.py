a, b, c = list(map(int, input().split()))
v = (a + b + c) // 3
print(abs(a - v) + abs(c - v))