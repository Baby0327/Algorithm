"""
369
"""

n = int(input())
result = 0

for i in range(1, n+1):
    result += str(i).count("3") + str(i).count("6") + str(i).count("9")

print(result)