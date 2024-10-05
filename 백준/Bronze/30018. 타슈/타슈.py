"""
타슈
"""

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
count = [0, 0]

for i, j in zip(a, b):
    if i > j:
        count[0] += (i - j)
    elif i < j:
        count[1] += (j - i)

print(max(count))