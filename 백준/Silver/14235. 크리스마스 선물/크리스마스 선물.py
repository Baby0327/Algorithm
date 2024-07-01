import sys

n = int(sys.stdin.readline())

present = []
for i in range(n):
    tmp = list(map(int, sys.stdin.readline().rstrip().split()))
    if tmp[0] != 0:
        for j in range(1,len(tmp)):
            present.append(tmp[j])
        present.sort()
    else:
        if len(present) == 0:
            print(-1)
        else:
            print(present[-1])
            del present[-1]