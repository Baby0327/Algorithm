N = int(input())
M = int(input())
total = []

for i in range(N,M+1):
    count = 0
    for j in range(1, i+1):
        if i % j == 0:
            count += 1
    if count == 2:
        total.append(i)

if len(total) != 0:
    print(sum(total))
    print(total[0])
else:
    print(-1)