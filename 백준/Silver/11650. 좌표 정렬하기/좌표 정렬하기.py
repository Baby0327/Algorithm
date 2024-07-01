XY = []
N = int(input())

for i in range(N):
    XY.append(list(map(int, input().split())))

XY.sort()

for x,y in XY:
    print(x,y)