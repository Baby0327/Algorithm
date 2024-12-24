n, m, k = map(int, input().split())
print(n // (k - m) + int(n % (k - m) > 0))