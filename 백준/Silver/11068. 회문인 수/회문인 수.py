import sys
input = sys.stdin.readline

def solution(n, j):
    num = []

    while n > 0:
        n, now = n // j, n % j
        num.append(now)

    return num == num[::-1]


for i in range(int(input())):
    n = int(input())
    check = 0

    for j in range(2, 65):
        if solution(n, j):
            check = 1
            break

    print(check)