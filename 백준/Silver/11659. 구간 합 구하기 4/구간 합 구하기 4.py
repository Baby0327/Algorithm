import sys

input = sys.stdin.readline
print = sys.stdout.write

n, m = map(int, input().split())

num = list(map(int, input().rstrip().split()))

total = 0
for i in range(n):
    total += num[i]
    num[i] = total

result = []
for i in range(m):
    start, end = map(int, input().split())
    if start == 1:
        print(str(num[end-1])+'\n')
    else:
        print(str(num[end-1]-num[start-2])+'\n')