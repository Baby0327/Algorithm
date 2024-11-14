import sys
input = sys.stdin.readline

n = int(input())
w = sorted(list(map(int, input().split())))
result = 1

for i in w:
    if result >= i:
        result += i
    else:
        break

print(result)