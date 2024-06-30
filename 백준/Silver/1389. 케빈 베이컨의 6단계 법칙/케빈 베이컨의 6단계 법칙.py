inf = int(100000000)

n, m = map(int, input().split())

relation = [[inf for i in range(n+1)] for y in range(n+1)]

for i in range(1, n+1):
    relation[i][i] = 0

for i in range(m):
    start, end = map(int, input().split())
    relation[start][end] = 1
    relation[end][start] = 1

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            relation[a][b] = min(relation[a][b], relation[a][k] + relation[k][b])

answer = inf
result = inf
for i in range(1, len(relation)):
    if sum(relation[i])-inf < answer:
        answer = sum(relation[i])-inf
        result = i
        
print(result)