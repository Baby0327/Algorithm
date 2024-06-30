import sys

N = int(sys.stdin.readline())
request = list(map(int, sys.stdin.readline().rstrip().split()))
M = int(sys.stdin.readline())

if sum(request) <= M:
    print(max(request))
else:
    left = 0
    right = max(request)
    result = 0

    while left <= right:
        middle = (left + right) // 2
        test = 0
        for i in request:
            if i > middle:
                test += middle
            else:
                test += i
        if test > M:
            right = middle - 1
        else:
            left = middle + 1
            result = max(middle, result)

    print(result)