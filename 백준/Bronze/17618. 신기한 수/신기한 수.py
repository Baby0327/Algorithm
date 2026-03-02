n = int(input())
m = [0] * (n + 1)
c = 0

for i in range(1, n + 1):
    m[i] = m[i // 10] + i % 10
    
    if i % m[i] == 0:
        c += 1

print(c)