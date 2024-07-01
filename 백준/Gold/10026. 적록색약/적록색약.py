import sys
from collections import deque


def bfs(input, x, y):
    queue = deque()
    queue.append([x, y])
    now = input[x][y]
    input[x][y] = 0

    while queue:
        tmp = queue.popleft()
        input[tmp[0]][tmp[1]] = 0
        for i in range(4):
            xx = tmp[0] + x_num[i]
            yy = tmp[1] + y_num[i]
            if xx < 0 or yy < 0 or xx >= len(input) or yy >= len(input):
                continue
            if input[xx][yy] == now:
                input[xx][yy] = 0
                queue.append([xx, yy])


def recursion(input, result):
    for i in range(N):
        for j in range(N):
            if input[i][j] != 0:
                bfs(input, i, j)
                result += 1
    return result

N = int(input())

graph1 = []
graph2 = []
for i in range(N):
    tmp = sys.stdin.readline().rstrip()
    graph1.append(list(tmp))
    graph2.append(list(tmp.replace("R", "G")))

x_num = [-1, 1, 0, 0]
y_num = [0, 0, -1, 1]

result1 = 0
output1 = recursion(graph1, result1)
result2 = 0
output2 = recursion(graph2, result2)

print(output1, output2)