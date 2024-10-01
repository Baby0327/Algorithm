"""
하얀 칸
"""

result = 0

for i in range(8):
    if i % 2:
        result += len([i for i in input()[1::2] if i == "F"])
    else:
        result += len([i for i in input()[::2] if i == "F"])

print(result)