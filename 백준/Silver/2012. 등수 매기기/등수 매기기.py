import sys

N = int(sys.stdin.readline())

num = [0 for i in range(N)]
for i in range(N):
    num[i] = int(sys.stdin.readline())

num.sort(reverse=True)

i = N
j = 0
result = 0
while j != N:
    tmp = num[j] - i
    if tmp >= 0:
        result += tmp
    else:
        result -= tmp
    i -= 1
    j += 1

print(result)