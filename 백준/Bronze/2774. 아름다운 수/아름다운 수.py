import sys

T = int(sys.stdin.readline())

result = []
for i in range(T):
    tmp = list(map(int, sys.stdin.readline().rstrip()))
    tmp = set(tmp)
    result.append(len(tmp))

for i in result:
    print(i)