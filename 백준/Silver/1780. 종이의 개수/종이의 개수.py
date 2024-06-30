def test(x, y, n):
    global first, second, third
    now = paper[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if paper[i][j] != now:
                test(x, y, n // 3)
                test(x + n // 3, y, n // 3)
                test(x + n // 3 * 2, y, n // 3)
                test(x , y + n // 3, n // 3)
                test(x + n // 3, y + n // 3, n // 3)
                test(x + n // 3 * 2, y + n // 3, n // 3)
                test(x , y + n // 3 * 2, n // 3)
                test(x + n // 3, y + n // 3 * 2, n // 3)
                test(x + n // 3 * 2, y + n // 3 * 2, n // 3)
                return 0
    if now == -1:
        first += 1
    elif now == 0:
        second += 1
    else:
        third += 1

n = int(input())
paper = []

for i in range(n):
    paper.append(list(map(int, input().split())))

first, second, third = 0, 0, 0
test(0, 0, n)

print(first)
print(second)
print(third)