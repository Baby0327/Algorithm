N, M = map(int, input().split())

result = []

a = 0
for i in range(N+1):
    result.append(a)
    a += 1

for x in range(M):
    i, j = map(int, input().split())
    count = 0
    for y in range((j-i)//2+(j-i)%2):
        tmp = result[i+count]
        result[i+count] = result[j-count]
        result[j-count] = tmp
        count += 1

for i in range(1, N + 1):
    print(result[i], end=" ")