"""
피보나치
"""

import sys

t = int(sys.stdin.readline())
fib = [0, 1]

for i in range(10000):
    fib.append(fib[-2] + fib[-1])

for i in range(t):
    p, q = map(int, sys.stdin.readline().split())

    sys.stdout.write(f"Case #{i + 1}: {fib[p] % q}\n")