"""
헌내기는 친구가 필요해
"""

import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

r = [-1, 0, 1, 0]
c = [0, 1, 0, -1]
campus = []
now = deque()

for i in range(n):
    campus.append(list(input().strip()))

    for j in range(len(campus[i])):
        if campus[i][j] == "I":
            now.append([i, j])
            campus[i][j] = "X"

count = 0

while now:
    for i in range(len(now)):
        y, x = now.popleft()

        for j in range(4):
            nr, nc = y + r[j], x + c[j]

            if 0 <= nr < n and 0 <= nc < m and campus[nr][nc] != "X":
                if campus[nr][nc] == "P":
                    count += 1

                campus[nr][nc] = "X"
                now.append([nr, nc])

print(count if count else "TT")