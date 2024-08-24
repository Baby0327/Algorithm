"""
내 학점을 구해줘
"""

t = int(input())

for i in range(t):
    n = int(input())
    total = 0
    div = 0

    for j in range(n):
        c, g = map(float, input().split())
        total += c * g
        div += c

    print(int(div), round(total / div, 1))