n, k = map(int, input().split())
result = []
now = 0

for i in range(n):
    a, b = map(int, input().split())
    now += (a - b)
    result.append(0 if now <= k else now - k)

print(max(result))
