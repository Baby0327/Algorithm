p = list(map(int, input().split()))
cnt = 0

while True:
    if p[2] - p[1] == p[1] - p[0] == 1:
        break

    if p[2] - p[1] >= p[1] - p[0]:
        p = [p[1], p[1] + 1, p[2]]
    else:
        p = [p[0], p[1] - 1, p[1]]

    cnt += 1

print(cnt)