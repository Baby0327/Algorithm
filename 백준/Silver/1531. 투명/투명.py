N, M = map(int, input().split())
test = [[0 for i in range(100)] for j in range(100)]

for i in range(N):
    lx, ly, rx, ry = map(int, input().split())
    for x in range(lx-1, rx):
        for y in range(ly-1, ry):
            test[x][y] += 1

result = 0
for x in range(100):
    for y in range(100):
        if test[x][y] > M:
            result += 1

print(result)