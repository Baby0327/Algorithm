import sys
input = sys.stdin.readline

k = int(input())
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
result = 0

for i in a:
    for j in b:
        if i + k == j:
            result += 1

print(result)