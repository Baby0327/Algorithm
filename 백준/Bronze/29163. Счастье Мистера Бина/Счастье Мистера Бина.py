"""
Mr. Bean's Happiness
"""

n = int(input())
num = list(map(int, input().split()))
odd = len([1 for i in num if i % 2 == 1])

print("Sad" if odd >= n - odd else "Happy")