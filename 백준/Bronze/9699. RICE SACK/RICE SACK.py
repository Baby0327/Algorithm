"""
RICE SACK
"""

import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
    print(f"Case #{i + 1}: {max(map(int, input().split()))}")