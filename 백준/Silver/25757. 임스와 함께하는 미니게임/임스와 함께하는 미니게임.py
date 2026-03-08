import sys
input = sys.stdin.readline

n, t = input().split()
c = len(set([input() for _ in range(int(n))]))

if t == "Y":
    print(c)
elif t == "F":
    print(c // 2)
else:
    print(c // 3)