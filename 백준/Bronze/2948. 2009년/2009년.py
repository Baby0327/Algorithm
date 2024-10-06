"""
2009년
"""

day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
result = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
d, m = map(int, input().split())

print(result[((sum(day[0:m - 1]) + d) + 2) % 7])