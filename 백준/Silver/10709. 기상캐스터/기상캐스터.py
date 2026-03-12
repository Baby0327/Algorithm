import sys
input = sys.stdin.readline

h, w = map(int, input().split())

for i in range(h):
    c = input().rstrip()
    p = [-1]

    for j in range(w):
        if c[j] == "c":
            p.append(0)
        else:
            p.append(-1 if p[-1] == -1 else p[-1] + 1)

    print(*p[1:])