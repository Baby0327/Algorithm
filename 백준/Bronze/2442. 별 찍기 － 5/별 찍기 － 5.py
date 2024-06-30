N = int(input())

for i in range(1, N + 1):
    tmp = '*' * (2 * i - 1)
    print(tmp.rjust(N+i-1, ' '))