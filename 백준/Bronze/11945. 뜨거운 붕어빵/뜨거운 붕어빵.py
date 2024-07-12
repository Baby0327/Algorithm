"""
뜨거운 붕어빵
"""

n, m = map(int, input().split())

for i in range(n):
    print("".join(list(input())[::-1]))