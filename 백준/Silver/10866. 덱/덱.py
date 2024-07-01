import sys
from collections import deque

N = int(input())

test = deque()

for i in range(N):
    tmp = sys.stdin.readline().split()
    if tmp[0] == 'push_front':
        test.appendleft(tmp[1])
    elif tmp[0] == 'push_back':
        test.append(tmp[1])
    elif tmp[0] == 'pop_front':
        if len(test) == 0:
            print(-1)
        else:
            print(test.popleft())
    elif tmp[0] == 'pop_back':
        if len(test) == 0:
            print(-1)
        else:
            print(test.pop())
    elif tmp[0] == 'size':
        print(len(test))
    elif tmp[0] == 'empty':
        if len(test) == 0:
            print(1)
        else:
            print(0)
    elif tmp[0] == 'front':
        if len(test) == 0:
            print(-1)
        else:
            print(test[0])
    elif tmp[0] == 'back':
        if len(test) == 0:
            print(-1)
        else:
            print(test[-1])