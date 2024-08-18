"""
경기 결과
"""

n = int(input())
A = 0
B = 0

for i in range(n):
    a, b = map(int, input().split())

    if a > b:
        A += 1
    elif a < b:
        B += 1

print(A, B)