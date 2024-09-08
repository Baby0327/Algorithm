"""
Batter Up
"""

n = int(input())
num = [i for i in list(map(int, input().split())) if i != -1]

print(sum(num) / len(num))