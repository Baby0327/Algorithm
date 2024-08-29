"""
최소, 최대 2
"""

t = int(input())

for i in range(t):
    n = int(input())
    num = list(map(int, input().split()))
    
    print(min(num), max(num))