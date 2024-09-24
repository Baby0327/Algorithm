"""
2진수 뒤집기
"""

n = int(input())

print(int(bin(n)[2:][::-1], 2))