"""
홀수일까 짝수일까
"""

import sys

n = int(sys.stdin.readline())

for i in range(n):
    sys.stdout.write("odd\n" if int(sys.stdin.readline()) %  2 else "even\n")