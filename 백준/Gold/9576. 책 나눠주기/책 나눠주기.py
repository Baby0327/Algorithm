import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().split())
    num = sorted([list(map(int, input().split())) for _ in range(m)], key=lambda x : (x[1]))
    book = [0] * (n + 1)
    cnt = 0

    for a, b in num:
        for i in range(a, b + 1):
            if not book[i]:
                book[i] = 1
                cnt += 1
                break

    print(cnt)