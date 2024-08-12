"""
점수계산
"""

n = int(input())
test = "".join(list(input().split())).split("0")
result = 0

for i in test:
    result += len(i) * (1 + len(i)) // 2

print(result)