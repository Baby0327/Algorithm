import sys
input = sys.stdin.readline

result = []

for i in range(int(input())):
    a, b = map(int, input().split())
    result.append(b // a)

print(min(result))