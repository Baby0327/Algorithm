import sys


def decimal(N):
    return num[N + 1:N * 2 + 1].count(True)


num = [True] * (123456 * 2 + 1)
num[0] = False
num[1] = False

for i in range(2, len(num)):
    if num[i]:
        for j in range(i + i, len(num) + 1, +i):
            num[j] = False
    else:
        continue

while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    else:
        print(decimal(n))
