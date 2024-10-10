"""
헌내기는 친구가 필요해
"""

import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

r = [-1, 0, 1, 0]
c = [0, 1, 0, -1]
visited = [[False for i in range(m)] for j in range(n)]
campus = []
now = deque()

for i in range(n):
    campus.append(list(input().strip()))

    for j in range(len(campus[i])):
        if campus[i][j] == 'I':
            now.append([i, j])
            visited[i][j] = True

count = 0

while now:
    for i in range(len(now)):
        y, x = now.popleft()

        for j in range(4):
            nr, nc = y + r[j], x + c[j]

            if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc] and campus[nr][nc] != 'X':
                if campus[nr][nc] == 'P':
                    count += 1

                visited[nr][nc] = True
                now.append([nr, nc])

print(count if count else "TT")