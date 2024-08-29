"""
더하기 4
"""

t = int(input())

for i in range(t):
    num = list(map(int, input().split()))

    print(sum(num))