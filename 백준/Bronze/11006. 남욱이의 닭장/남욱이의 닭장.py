"""
남욱이의 닭장
"""

t = int(input())

for i in range(t):
    n, m = map(int, input().split())

    print(m * 2 - n, n - m)