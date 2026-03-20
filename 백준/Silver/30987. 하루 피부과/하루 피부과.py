x1, x2 = map(int, input().split())
a, b, c, d, e = map(int, input().split())
n = [(c - e), (1/2) * (b - d), (1/3) * a]
print(int((n[0] * x2 + n[1] * x2**2 + n[2] * x2**3) - (n[0] * x1 + n[1] * x1**2 + n[2] * x1**3)))