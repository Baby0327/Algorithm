"""
MBTI
"""

mbti = input()
n = int(input())
count = 0

for i in range(n):
    if mbti == input():
        count += 1

print(count)