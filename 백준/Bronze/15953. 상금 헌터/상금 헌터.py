import sys
input = sys.stdin.readline

first = [[500, 1], [300, 3], [200, 6], [50, 10], [30, 15], [10, 21]]
second = [[512, 1], [256, 3], [128, 7], [64, 15], [32, 31]]

for _ in range(int(input())):
    a, b = map(int, input().split())

    if a == 0:
        a = 100
    if b == 0:
        b = 100

    p1 = list(filter(lambda x : x[1] >= a, first))[0][0] if a <= 21 else 0
    p2 = list(filter(lambda x : x[1] >= b, second))[0][0] if b <= 31 else 0
    print((p1 + p2) * 10000)