import sys
input = sys.stdin.readline

while 1:
    a, *t = list(map(int, input().split()))
    l = 1

    if not a:
        break

    for i in range(a):
        l *= t[2 * i]
        l -= t[2 * i + 1]

    print(l)