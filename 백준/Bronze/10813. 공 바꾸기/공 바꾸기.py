N, M = map(int, input().split())

result = []

a = 0
for i in range(N+1):
    result.append(a)
    a += 1

for x in range(M):
    i, j = map(int, input().split())
    tmp = result[i]
    result[i] = result[j]
    result[j] = tmp

for i in range(1,N+1):
    print(result[i], end=" ")