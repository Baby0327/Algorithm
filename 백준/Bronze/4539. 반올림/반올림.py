import sys

n = int(sys.stdin.readline().rstrip())

result = []
for i in range(n):
    tmp = sys.stdin.readline().rstrip()
    tmp = list(map(int, tmp))
    test = 0
    for j in range(len(tmp) - 1, 0, -1):
        if tmp[j] >= 5:
            tmp[j - 1] += 1
            tmp[j] = 0
        else:
            tmp[j] = 0

    test = "".join(map(str, tmp))
    result.append(test)

for i in result:
    print(i)