"""
내려가기
"""

import sys
input = sys.stdin.readline

n = int(input())
start = list(map(int, input().split()))
maxi, mini = start, start

for i in range(n - 1):
    temp = list(map(int, input().split()))
    maxi = [temp[0] + max(maxi[0:2]), temp[1] + max(maxi), temp[2] + max(maxi[1:])]
    mini = [temp[0] + min(mini[0:2]), temp[1] + min(mini), temp[2] + min(mini[1:])]

print(max(maxi), min(mini))