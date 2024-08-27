"""
Angles
"""

n = int(input())

for i in range(n):
    angles = list(map(int, input().split()))

    if sum(angles) == 180:
        result = "Seems OK"
    else:
        result = "Check"

    print(*angles, result)