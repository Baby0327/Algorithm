l = int(input())
n = int(input())
cake = [0 for _ in range(l)]
result1 = [0, 0]
result2 = 0
maxi = 0

for i in range(1, n + 1):
    a, b = map(int, input().split())
    cnt = 0

    if b - a + 1 > result1[1]:
        result1 = [i, b - a + 1]

    for j in range(a - 1, b):
        if not cake[j]:
            cake[j] = i
            cnt += 1

    if cnt > maxi:
        result2 = i
        maxi = cnt

print(result1[0])
print(result2)