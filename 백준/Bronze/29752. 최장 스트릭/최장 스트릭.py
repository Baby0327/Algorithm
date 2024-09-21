"""
최장 스트릭
"""

n = int(input())
temp = 0
result = 0
s = list(map(int, input().split()))

for i in s:
    if i != 0:
        temp += 1
    else:
        result = max(result, temp)
        temp = 0

result = max(result, temp)

print(result)