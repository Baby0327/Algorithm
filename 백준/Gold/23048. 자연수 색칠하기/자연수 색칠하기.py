num = [0] * 500001
num[0] = 0
num[1] = 1

color = 2
for i in range(2, 500001):
    if num[i] == 0:
        for j in range(i, 500001, +i):
            num[j] = color
        color += 1

N = int(input())

print(max(num[1:N+1]))

for i in range(1, N + 1):
    print(num[i], end=" ")