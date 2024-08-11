"""
거북이
"""

num = list(map(int, input().split()))
num.sort()

print(num[0] * num[2])