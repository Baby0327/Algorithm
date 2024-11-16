import sys
input = sys.stdin.readline

result = [0] * 4

for i in range(int(input())):
    g, c, n = map(int, input().split())

    if g == 1:
        result[3] += 1
    elif c in (1, 2):
        result[0] += 1
    elif c == 3:
        result[1] += 1
    else:
        result[2] += 1

for i in result:
    print(i)