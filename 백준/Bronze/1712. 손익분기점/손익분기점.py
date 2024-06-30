a, b, c = map(int, input().split())

if b >= c:
    print(-1)
else:
    result = a / (c - b)
    result = int(result) + 1
    print(result)