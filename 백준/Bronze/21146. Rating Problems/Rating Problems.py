n, k = map(int, input().split())
total = sum(int(input()) for _ in range(k))
print((total + (n - k) * -3) / n, (total + (n - k) * 3) / n)