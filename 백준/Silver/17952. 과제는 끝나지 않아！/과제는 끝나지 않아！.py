import sys

N = int(sys.stdin.readline())

working = []
result = 0
for i in range(1, N+1):
    tmp = list(map(int, sys.stdin.readline().split()))
    if tmp[0] == 0:
        if len(working) == 0:
            continue
        else:
            working[-1][-1] -= 1
    else:
        working.append(tmp)
        working[-1][-1] -= 1

    if working[-1][-1] == 0:
        result += working[-1][1]
        working.pop()

print(result)