"""
Every Second Counts
"""

time1 = list(map(int, input().split(":")))
time2 = list(map(int, input().split(":")))
total1, total2 = 0, 0

for i in range(3):
    total1 += time1[i] * (60 ** (2-i))
    total2 += time2[i] * (60 ** (2-i))

# 앞의 시간이 뒤의 시간보다 총합이 클 때, 24시간을 계산에 반영함
if total1 > total2:
    total2 += 24 * 60**2

print(total2 - total1)