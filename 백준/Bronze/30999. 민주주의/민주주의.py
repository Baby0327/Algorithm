"""
민주주의
"""

n, m = map(int, input().split())
result = 0

for i in range(n):
    if input().count("O") > (m // 2):
        result += 1

print(result)