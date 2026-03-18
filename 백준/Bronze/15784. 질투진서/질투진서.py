import sys
input = sys.stdin.readline

n, a, b = map(int, input().split())
s = []
j = 0

for i in range(n):
    l = list(map(int, input().split()))

    if i == a - 1:
        s += l
        j = l[b - 1]
    else:
        s.append(l[b - 1])

print("HAPPY" if j >= max(s) else "ANGRY")