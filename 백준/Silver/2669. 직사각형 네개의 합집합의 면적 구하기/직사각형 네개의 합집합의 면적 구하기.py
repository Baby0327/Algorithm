import sys

test = [[0 for i in range(100)] for j in range(100)]

for i in range(4):
    lx, ly, rx, ry = map(int, sys.stdin.readline().split())
    for x in range(lx, rx):
        for y in range(ly, ry):
            test[x][y] += 1

result = 0
for x in range(100):
    for y in range(100):
        if test[x][y] != 0:
            result += 1

print(result)