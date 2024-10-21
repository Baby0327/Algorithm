"""
아이스크림 (Ice Cream)
"""

s = int(input())
a = int(input())
b = int(input())

if s <= a:
    print(250)
else:
    print(250 + (s - a) // b * 100 if (s - a) % b == 0 else 250 +  ((s - a) // b + 1) * 100)