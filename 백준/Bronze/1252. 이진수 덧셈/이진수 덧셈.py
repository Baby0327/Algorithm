"""
이진수 덧셈
"""

a, b = input().split()
result = int(a, 2) + int(b, 2)

print(bin(result)[2:])