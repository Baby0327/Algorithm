"""
회전
"""

n = input()
result = 0

for i in range(1, len(n)):
    result += int(n[i:] + n[:i])

print(result + int(n))