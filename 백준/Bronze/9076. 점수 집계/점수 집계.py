"""
점수 집계
"""

t = int(input())

for i in range(t):
    n = sorted(list(map(int, input().split())))[1:4]

    print(sum(n) if n[2] - n[0] < 4 else "KIN")