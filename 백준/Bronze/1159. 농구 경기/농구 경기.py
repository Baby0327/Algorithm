"""
농구 경기
"""

n = int(input())
count = {}

for i in range(n):
    name = input()[0]
    count[name] = count.get(name, 0) + 1

result = ""

for k, v in count.items():
    if v >= 5:
        result += k

print("".join(sorted(result)) if len(result) > 0 else "PREDAJA")