n = int(input())
h = list(map(int, input().split()))
t = 1000001
c = 1

for i in range(n):
    if h[i] >= t:
        c += 1
    t = h[i]

print(c)