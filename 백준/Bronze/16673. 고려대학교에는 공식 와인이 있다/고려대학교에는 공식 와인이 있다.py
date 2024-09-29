"""
고려대학교에는 공식 와인이 있다
"""

c, k, p = map(int, input().split())

print(sum([k * i + p * (i**2) for i in range(c + 1)]))