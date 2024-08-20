"""
전자레인지
"""

t = int(input())

s300 = t // 300
s60 = t % 300 // 60
s10 = t % 60 // 10

if t % 10:
    print(-1)
else:
    print(s300, s60, s10)