import sys
from collections import deque

N = int(sys.stdin.readline())

list = deque()
for i in range(N):
    tmp = sys.stdin.readline().rstrip().split()

    if tmp[0] == "push":
        list.append(int(tmp[1]))
    elif tmp[0] == "pop":
        if len(list) == 0:
            print(-1)
        else:
            print(list.popleft())
    elif tmp[0] == "size":
        print(len(list))
    elif tmp[0] == "empty":
        if len(list) == 0:
            print(1)
        else:
            print(0)
    elif tmp[0] == "front":
        if len(list) == 0:
            print(-1)
        else:
            print(list[0])
    elif tmp[0] == "back":
        if len(list) == 0:
            print(-1)
        else:
            print(list[-1])