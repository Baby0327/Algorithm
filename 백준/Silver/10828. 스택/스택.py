import sys
from collections import deque

N = int(sys.stdin.readline())
result = deque()

for i in range(N):
    tmp = sys.stdin.readline().split()
    if tmp[0] == 'push':
        result.append(tmp[1])
    elif tmp[0] == 'pop':
        if len(result) == 0:
            print(-1)
        else:
            print(result.pop())
    elif tmp[0] == 'size':
        print(len(result))
    elif tmp[0] == 'empty':
        if len(result) == 0:
            print(1)
        else:
            print(0)
    elif tmp[0] == 'top':
        if len(result) == 0:
            print(-1)
        else:
            print(result[-1])