"""
숫자 빈도수
"""

n, d = map(int, input().split())
count = 0

for i in range(1, n+1):
    count += str(i).count(str(d))

print(count)