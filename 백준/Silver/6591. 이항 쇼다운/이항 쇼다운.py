import sys

while True:
    left, right = map(int, sys.stdin.readline().split())

    if left == right == 0:
        break

    if left - right < right:
        right = left - right

    top = 1
    for i in range(left, left-right, -1):
        top *= i

    bottom = 1
    for i in range(1, right+1):
        bottom *= i

    print(top//bottom)