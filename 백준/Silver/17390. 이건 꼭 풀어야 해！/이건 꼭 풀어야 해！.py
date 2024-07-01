import sys

n, q = map(int, sys.stdin.readline().split())
tmp = list(map(int, sys.stdin.readline().split()))
tmp.sort()
sum = 0
num = [0 for i in range(n+1)]

for i in range(1, n+1):
    sum += tmp[i-1]
    num[i] = sum

for i in range(q):
    start, end = map(int, sys.stdin.readline().split())
    result = num[end] - num[start-1]
    sys.stdout.write(str(result)+"\n")