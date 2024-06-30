def test(x, y, n):
    global white, blue
    color = paper[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if paper[i][j] != color:
                test(x, y,n//2)
                test(x, y+n//2, n//2)
                test(x+n//2, y, n//2)
                test(x+n//2, y+n//2, n//2)
                return 0
    if color == 0:
        white += 1
    else:
        blue += 1

n = int(input())
paper = []
for i in range(n):
    paper.append(list(map(int, input().split())))
white = 0
blue = 0
test(0, 0, n)
print(white)
print(blue)