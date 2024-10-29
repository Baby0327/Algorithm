import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
result = [-1] * n
stack = []
count = [0] * 1000001

for i in a:
    count[i] += 1

for i in range(n):
    while stack and count[a[stack[-1]]] < count[a[i]]:
        result[stack.pop()] = a[i]
    stack.append(i)

print(" ".join(map(str, result)))