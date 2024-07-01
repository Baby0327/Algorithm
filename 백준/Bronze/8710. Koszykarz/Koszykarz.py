k, w, m = map(int, input().split())
result = w - k
if result % m == 0:
    result = result//m
else:
    result = result//m + 1
print(result)