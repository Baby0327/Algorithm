import sys

N, M = map(int, sys.stdin.readline().rstrip().split())

search = {}

for i in range(N):
    site, password = map(str, sys.stdin.readline().rstrip().split())
    search[site] = password

result = []
for i in range(M):
    tmp = sys.stdin.readline().rstrip()
    result.append(search[tmp])

for i in result:
    print(i)