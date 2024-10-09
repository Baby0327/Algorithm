"""
카드 역배치
"""

num = [i for i in range(1, 21)]

for i in range(10):
    a, b = map(int, input().split())
    num = num[:a - 1] + num[a - 1:b][::-1] + num[b:]

print(*num)