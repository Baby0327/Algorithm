import sys

input = sys.stdin.readline

n = int(input())

result = {}
for i in range(n):
    tmp = list(input().rstrip().split('.'))
    if tmp[1] in result.keys():
        result[tmp[1]] += 1
    else:
        result[tmp[1]] = 1

name = list(result)
name.sort()

for i in name:
    print(i, result[i])