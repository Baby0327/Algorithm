import sys

N = int(sys.stdin.readline())

test = []
for i in range(N):
    tmp = list(map(int, sys.stdin.readline().rstrip().split()))
    if tmp[0] == 1:
        test.append(tmp[1])
    elif tmp[0] == 2:
        if len(test) != 0:
            result = test.pop()
            print(result)
        else:
            print(-1)
    elif tmp[0] == 3:
        print(len(test))
    elif tmp[0] == 4:
        if len(test) == 0:
            print(1)
        else:
            print(0)
    elif tmp[0] == 5:
        if len(test) != 0:
            print(test[-1])
        else:
            print(-1)