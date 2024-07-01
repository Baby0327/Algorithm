import sys

N = int(sys.stdin.readline())

num = []

for i in range(N):
    x, y = map(int, sys.stdin.readline().split())
    num.append([x, y])

num.sort(key = lambda x: (x[1], x[0]))

for i in num:
    print(i[0], i[1])