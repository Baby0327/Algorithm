from collections import deque

n = int(input())

test = deque([i for i in range(1, n+1)])

while len(test) > 0:
    print(test.popleft(), end=" ")
    test.rotate(-1)