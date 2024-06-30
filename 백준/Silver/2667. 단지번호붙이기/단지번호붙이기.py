import sys
from collections import deque


def bfs(input, x, y):
    queue = deque()
    queue.append([x, y])
    graph[x][y] = 0
    count = 1

    while queue:
        tmp = queue.popleft()
        graph[tmp[0]][tmp[1]] = 0
        for i in range(4):
            xx = tmp[0] + x_num[i]
            yy = tmp[1] + y_num[i]
            if xx < 0 or yy < 0 or xx >= len(graph) or yy >= len(graph):
                continue
            if graph[xx][yy] == 1:
                graph[xx][yy] = 0
                queue.append([xx, yy])
                count += 1
    return count


N = int(input())

graph = []
for i in range(N):
    graph.append(list(map(int, sys.stdin.readline().rstrip())))

result = []
x_num = [-1, 1, 0, 0]
y_num = [0, 0, -1, 1]

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            count = bfs(graph, i, j)
            result.append(count)

print(len(result))
result.sort()
for i in result:
    print(i)