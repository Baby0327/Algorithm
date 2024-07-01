import sys
input = sys.stdin.readline

r, c, q = map(int, input().split())
tmp = []
for i in range(r):
    tmp.append(list(map(int, input().split())))

photo = [[0 for i in range(c+1)] for j in range(r+1)]
photo[1][1] = tmp[0][0]

for i in range(1, r+1):
    for j in range(1, c+1):
        photo[i][j] = photo[i-1][j] + photo[i][j-1] - photo[i-1][j-1] + tmp[i-1][j-1]

for i in range(q):
    x1, y1, x2, y2 = map(int, input().split())
    part = photo[x2][y2] - photo[x2][y1-1] - photo[x1-1][y2] + photo[x1-1][y1-1]
    count = (x2-x1+1)*(y2-y1+1)
    sys.stdout.write(str(part//count)+'\n')