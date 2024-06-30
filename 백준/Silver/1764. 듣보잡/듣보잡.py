import sys

N, M = map(int, sys.stdin.readline().split())

name1 = set()
for i in range(N):
    name1.add(sys.stdin.readline().rstrip())

name2 = set()
for i in range(M):
    name2.add(sys.stdin.readline().rstrip())

result = name1 & name2

print(len(result))

result = list(result)
result.sort()

for i in result:
    print(i)