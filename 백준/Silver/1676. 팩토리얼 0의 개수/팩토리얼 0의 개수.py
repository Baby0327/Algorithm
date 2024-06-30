N = int(input())

result = 1
for i in range(N, 0, -1):
    result *= i

result = list(map(int, str(result)))

i = -1
count = 0
while True:
    if result[i] == 0:
        count += 1
        i -= 1
    else:
        break

print(count)