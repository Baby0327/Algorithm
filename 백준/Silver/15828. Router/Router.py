"""
Router
"""

from collections import deque

n = int(input())
buffer = deque()

while True:
    num = int(input())

    if num == -1:
        break
    elif num == 0:
        buffer.popleft()
    else:
        if len(buffer) == n:
            continue
        else:
            buffer.append(num)

print(*buffer if len(buffer) > 0 else "empty")