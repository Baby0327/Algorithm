import sys
input = sys.stdin.readline

n = int(input())
box = list(map(int, input().split()))
result = [1] * n

for i in range(n):
    for j in range(i):
        if box[j] < box[i]:
            result[i] = max(result[i], result[j] + 1)

print(max(result))