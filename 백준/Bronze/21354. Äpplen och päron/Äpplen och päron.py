"""
사과와 배
"""

a, p = map(int, input().split())
result1 = 7 * a
result2 = 13 * p

if result1 > result2:
    print("Axel")
elif result1 < result2:
    print("Petra")
else:
    print("lika")