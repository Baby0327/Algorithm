"""
Quadrilateral
"""

t = int(input())

for i in range(t):
    w, h = map(int, input().split())
    for j in range(h):
        print("X" * w)
    print()