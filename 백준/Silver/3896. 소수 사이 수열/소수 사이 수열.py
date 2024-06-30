import sys

decimal = [True]*1299710
decimal[0] = False
decimal[1] = False

for i in range(2, 1299710):
    if decimal[i]:
        for j in range(i+i, 1299710, +i):
            decimal[j] = False

T = int(sys.stdin.readline())

for i in range(T):
    n = int(sys.stdin.readline())
    if decimal[n]:
        print(0)
    else:
        right = 1
        while not decimal[n+right]:
            right += 1

        left = 1
        while not decimal[n-left]:
            left += 1

        print(left + right)