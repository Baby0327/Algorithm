import sys

N = int(input())

total = 0
for i in range(N):
    tmp = int(sys.stdin.readline())
    total += tmp

print(total-N+1)