"""
N M 찍기
"""

n, m = map(int, input().split())
num = 1

for i in range(n):
    temp = []
    for j in range(m):
        temp.append(num)
        num += 1
    print(*temp)