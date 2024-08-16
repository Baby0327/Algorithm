"""
오각형, 오각형, 오각형...
"""

n = int(input())
num = [5]

for i in range(2, n+1):
    num.append((num[-1] + 2*i + (i+1)) % 45678)

print(num[-1])