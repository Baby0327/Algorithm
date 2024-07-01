import sys

N, M = map(int, sys.stdin.readline().split())
tmp = []

for i in range(N):
    tmp.append(list(map(int, sys.stdin.readline().split())))

graph = [[0 for i in range(N+1)] for j in range(N+1)]
for i in range(1, N+1):
    for j in range(1, N+1):
        graph[i][j] = graph[i-1][j] + graph[i][j-1] - graph[i-1][j-1] + tmp[i-1][j-1]

for i in range(M):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    result = graph[x2][y2] - graph[x2][y1-1] - graph[x1-1][y2] + graph[x1-1][y1-1]
    sys.stdout.write(str(result)+'\n')