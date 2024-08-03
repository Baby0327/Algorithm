"""
Dog Treats
"""

result = 0

for i in range(3):
    result += int(input()) * (i+1)

print("happy" if result >= 10 else "sad")