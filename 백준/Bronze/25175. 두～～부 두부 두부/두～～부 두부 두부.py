n, m, k = map(int, input().split())
result = (m + k - 3) % n
print(result if result else n)