a, b, c = map(int, input().split())
count = [0 for i in range(16001)]

for i in range(1, a+1):
    for j in range(1, b+1):
        for k in range(1, c+1):
            count[i+j+k] += 1

print(count.index(max(count)))