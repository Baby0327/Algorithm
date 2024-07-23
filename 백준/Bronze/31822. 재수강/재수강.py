"""
재수강
"""

code, num = map(str, input().split("-"))
n = int(input())
count = 0

for i in range(n):
    if code[:5] == input()[:5]:
        count += 1

print(count)