n = int(input())
i = list(map(int, input().split()))
result = 0

for j in range(n):
    x, y = map(int, input().split())
    if i[j] and y > x:
        result += y - x

print(result)