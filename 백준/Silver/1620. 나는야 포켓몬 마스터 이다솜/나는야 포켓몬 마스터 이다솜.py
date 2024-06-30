import sys

N, M = map(int, sys.stdin.readline().split())

name = {}
for i in range(1, N+1):
    tmp = sys.stdin.readline().rstrip()
    name[i] = tmp

reverse_name = dict(map(reversed, name.items()))

result = []
for i in range(M):
    tmp = sys.stdin.readline().rstrip()
    if tmp.isalpha():
        result.append(reverse_name[tmp])
    elif tmp.isdigit():
        result.append(name[int(tmp)])

for i in result:
    print(i)
