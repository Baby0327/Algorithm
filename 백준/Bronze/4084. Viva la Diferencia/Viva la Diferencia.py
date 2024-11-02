import sys
input = sys.stdin.readline

while True:
    a, b, c, d = map(int, input().split())
    cnt = 0

    if a == b == c == d == 0:
        break

    while not (a == b == c == d):
        a, b, c, d = map(abs, (a - b, b - c, c - d, d - a))
        cnt += 1

    print(cnt)