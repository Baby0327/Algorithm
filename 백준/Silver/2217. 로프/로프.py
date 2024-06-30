import sys

input = sys.stdin.readline

n = int(input())
test = []
for i in range(n):
    test.append(int(input()))

test.sort()

result = 0
for i in range(len(test)):
    tmp = test[i]*(len(test)-i)
    result = max(tmp, result)

print(result)