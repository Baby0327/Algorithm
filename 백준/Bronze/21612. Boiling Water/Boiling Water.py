b = int(input())
p = 5 * b - 400
n = 1 if p < 100 else -1
print(p)
print((n if p != 100 else 0))