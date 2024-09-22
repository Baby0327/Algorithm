"""
학번
"""

n = int(input())

for i in range(n):
    g = int(input())
    num = []

    for j in range(g):
        num.append(int(input()))

    result = 1

    while len(set([i % result for i in num])) != g:
        result += 1

    print(result)