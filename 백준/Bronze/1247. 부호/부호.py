"""
부호
"""

import sys

for i in range(3):
    n = int(sys.stdin.readline())
    result = 0

    for j in range(n):
        result += int(sys.stdin.readline())

    if result < 0:
        print("-")
    elif result == 0:
        print("0")
    else:
        print("+")