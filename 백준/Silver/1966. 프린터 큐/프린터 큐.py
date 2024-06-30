import sys
from collections import deque

T = int(sys.stdin.readline())

for i in range(T):
    N, M = map(int, sys.stdin.readline().split())
    priority = deque(list(map(int, sys.stdin.readline().rstrip().split())))
    tmp = deque([0 for x in range(N)])
    tmp[M] = 1

    count = 0

    while True:
        if priority[0] == max(priority):
            priority.popleft()
            tmp.popleft()
            count += 1
        else:
            tmp.rotate(-1)
            priority.rotate(-1)

        if 1 not in tmp:
            print(count)
            break