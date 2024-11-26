import sys
input = sys.stdin.readline

for i in range(int(input())):
    n = int(input())
    result = 0

    for j in range(n):
        result += (n - j) ** 2

    print(result)