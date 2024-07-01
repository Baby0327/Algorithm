import sys

M = int(sys.stdin.readline())
S = set()

for i in range(M):
    tmp = sys.stdin.readline().rstrip().split()
    if tmp[0] == 'add':
        if int(tmp[1]) in S:
            continue
        else:
            S.add(int(tmp[1]))
    elif tmp[0] == 'remove':
        if int(tmp[1]) in S:
            S.remove(int(tmp[1]))
        else:
            continue
    elif tmp[0] == 'check':
        if int(tmp[1]) in S:
            print(1)
        else:
            print(0)
    elif tmp[0] == 'toggle':
        if int(tmp[1]) in S:
            S.remove(int(tmp[1]))
        else:
            S.add(int(tmp[1]))
    elif tmp[0] == 'all':
        S = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}
    elif tmp[0] == 'empty':
        S = set()