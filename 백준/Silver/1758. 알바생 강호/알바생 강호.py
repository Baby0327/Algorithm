import sys

N = int(sys.stdin.readline())

num = []
for i in range(N):
    num.append(int(sys.stdin.readline()))

num.sort(reverse=True)

result = []
i = 0
tmp = 0
while True:
    if i == len(num):
        break
    tmp = num[i]-i
    if tmp < 0:
        break
    else:
        result.append(tmp)
    i += 1

print(sum(result))