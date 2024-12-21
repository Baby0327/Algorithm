import sys
input = sys.stdin.readline

n, k, l = map(int, input().split())
result = []
cnt = 0

for i in range(n):
    x = list(map(int, input().split()))

    if len(list(filter(lambda a : a >= l, x))) == 3 and sum(x) >= k:
        result += x
        cnt += 1

print(cnt)
print(*result)