import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    result = 0

    for i in range(n):
        result += max(list(map(int, input().split())) + [0])

    print(result)