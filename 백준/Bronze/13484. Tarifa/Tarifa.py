import sys
input = sys.stdin.readline

x = int(input())
result = x

for i in range(int(input())):
    result += x - int(input())

print(result)