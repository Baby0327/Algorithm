import sys
input = sys.stdin.readline

for _ in range(int(input())):
    j, n = map(int, input().split())
    s = []

    for i in range(n):
        r, c = map(int, input().split())
        s.append(r * c)

    s.sort(reverse=True)
    cnt, i = 0, 0

    while cnt < j:
        cnt += s[i]
        i += 1

    print(i)