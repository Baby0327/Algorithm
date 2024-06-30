import sys

result = []

while True:
    tmp = list(sys.stdin.readline().rstrip())
    if tmp == ['0']:
        break
    tmp = list(map(int, tmp))
    total = 0
    for i in tmp:
        if i == 1:
            total += 2
        elif i == 0:
            total += 4
        else:
            total += 3
    total += (len(tmp) + 1)
    result.append(total)

for i in result:
    print(i)