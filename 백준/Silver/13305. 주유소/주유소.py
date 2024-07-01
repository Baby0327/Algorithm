import sys

N = int(sys.stdin.readline())
length = list(map(int, sys.stdin.readline().rstrip().split()))
cost = list(map(int, sys.stdin.readline().rstrip().split()))

before = cost[0]
result = before*length[0]

for i in range(1, len(cost)-1):
    if cost[i] < before:
        result += cost[i]*length[i]
        before = cost[i]
    else:
        result += before*length[i]

print(result)