"""
Zero or One
"""

num = list(map(int, input().split()))
result = "*"

for i in num:
    if num.count(i) == 1:
        result = chr(65 + num.index(i))
        break

print(result)