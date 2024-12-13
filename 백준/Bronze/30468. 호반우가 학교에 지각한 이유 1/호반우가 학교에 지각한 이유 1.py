n = list(map(int, input().split()))
result = n[-1] * 4 - sum(n[:-1])
print(result if result > 0 else 0)