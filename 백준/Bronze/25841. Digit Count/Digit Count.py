"""
Digit Count
"""

start, end, num = map(int, input().split())
count = 0

for i in range(start, end+1):
    count += str(i).count(str(num))

print(count)