import sys
input = sys.stdin.readline

for _ in range(int(input())):
    a, b = sorted(list(map(int, input().split())))
    A, B = str(a), str(b)
    l = len(B) - len(A)
    result = ""

    for i in range(len(B)):
        if i < l:
            result += B[i]
        else:
            result += str(int(A[i - l]) * int(B[i]))

    print(1 if int(result) == a * b else 0)