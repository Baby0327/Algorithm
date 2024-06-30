import sys

result = []
while True:
    count = 0
    tmp1 = list(map(int, sys.stdin.readline().rstrip().split()))
    if tmp1 == [-1]:
        break
    for i in tmp1:
        if i*2 in tmp1:
            count += 1
    result.append(count-1)

for i in result:
    print(i)