import sys

N, M = map(int, sys.stdin.readline().split())

price = []
for i in range(M):
    price.append(int(sys.stdin.readline()))

price.sort()

num = min(N, M)

i = 1
result = price[0]*num
pay = price[0]
while i != len(price):
    count = 0
    for j in price:
        if j < price[i]:
            count += 1
        else:
            break
    if num < M-count:
        total = price[i]*num
    else:
        total = price[i]*(M-count)
    if total > result:
        result = total
        pay = price[i]
    i += 1

print(pay, result)