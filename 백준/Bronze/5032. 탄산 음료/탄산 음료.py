e, f, c = map(int, input().split())
now = e + f
cnt = 0

while now >= c:
    cnt += now // c
    now = now % c + now // c

print(cnt)