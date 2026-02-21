p, m = map(int, input().split())
result = -1

for i in range(p + 1):
    if p - i - i == m:
        result = i
        break

if result >= 0:
    print(p - result, result)
else:
    print(result)