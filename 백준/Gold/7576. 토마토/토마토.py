from collections import deque


def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            xx, yy = x + x_num[i], y + y_num[i]
            if (0 <= xx < n) and (0 <= yy < m) and (tomato[xx][yy] == 0):
                tomato[xx][yy] = tomato[x][y] + 1
                queue.append([xx, yy])


m, n = map(int, input().split())
tomato = [list(map(int, input().split())) for i in range(n)]
queue = deque([])

for i in range(n):
    for j in range(m):
        if tomato[i][j] == 1:
            queue.append([i, j])

x_num, y_num = [-1, 1, 0, 0], [0, 0, -1, 1]

bfs()

day = 0
for i in tomato:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    day = max(day, max(i))

print(day - 1)