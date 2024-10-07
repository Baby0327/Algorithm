"""
Donation Packaging
"""

import sys
input = sys.stdin.readline

t = int(input())
p = [0, 0, 0]

for i in range(t):
    now = list(map(int, input().split()))

    for j in range(3):
        p[j] += now[j]

    result = min(p)
    
    if result >= 30:
        print(result)
        
        for j in range(3):
            p[j] -= result
    else:
        print("NO")