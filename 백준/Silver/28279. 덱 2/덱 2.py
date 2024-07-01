import sys
from collections import deque

N = int(sys.stdin.readline())

test = deque()
for i in range(N):
    tmp = list(map(int, sys.stdin.readline().rstrip().split()))
    if tmp[0] == 1:
        test.appendleft(tmp[1])
    elif tmp[0] == 2:
        test.append(tmp[1])
    elif tmp[0] == 3:
        if len(test) != 0:
            result = test.popleft()
            print(result)
        else:
            print(-1)
    elif tmp[0] == 4:
        if len(test) != 0:
            result = test.pop()
            print(result)
        else:
            print(-1)
    elif tmp[0] == 5:
        print(len(test))
    elif tmp[0] == 6:
        if len(test) == 0:
            print(1)
        else:
            print(0)
    elif tmp[0] == 7:
        if len(test) != 0:
            print(test[0])
        else:
            print(-1)
    elif tmp[0] == 8:
        if len(test) != 0:
            print(test[-1])
        else:
            print(-1)