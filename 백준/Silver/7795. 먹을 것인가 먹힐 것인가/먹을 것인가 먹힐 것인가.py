import sys

T = int(sys.stdin.readline())

for i in range(T):
    N, M = map(int, sys.stdin.readline().split())
    A = list(map(int, sys.stdin.readline().split()))
    B = list(map(int, sys.stdin.readline().split()))
    B.sort()
    count = 0
    for x in A:
        left = 0
        right = M - 1
        tmp = -1
        while left <= right:
            middle = (left + right) // 2
            if B[middle] < x:
                left = middle + 1
                tmp = middle
            else:
                right = middle - 1
        count += tmp + 1
    print(count)