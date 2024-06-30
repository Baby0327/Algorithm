from collections import deque

N = int(input())
result = deque(range(1, N + 1))

while len(result) != 1:
    result.popleft()
    result.rotate(-1)

print(result[0])