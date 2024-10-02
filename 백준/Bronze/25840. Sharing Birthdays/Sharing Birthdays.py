"""
Sharing Birthdays
"""

n = int(input())
date = set()

for i in range(n):
    date.add(input())

print(len(date))