N = int(input())
paper = [[0 for i in range(100)] for j in range(100)]

for i in range(N):
    left, bottom = map(int, input().split())
    for x in range(left, left+10):
        for y in range(bottom, bottom+10):
            paper[x][y] = 1

result = 0

for i in range(100):
    for j in range(100):
        result += paper[i][j]

print(result)