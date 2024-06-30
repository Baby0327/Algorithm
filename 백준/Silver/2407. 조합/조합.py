n, m = map(int, input().split())

top = 1
for i in range(n, n-m, -1):
    top *= i

bottom = 1
for i in range(1, m+1):
    bottom *= i

print(top//bottom)