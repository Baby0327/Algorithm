"""
암호제작
"""

p, k = map(int, input().split())
result = True
num = 0

for i in range(2, k):
    if p % i == 0:
        result = False
        num = i
        break

if result:
    print("GOOD")
else:
    print("BAD", num)