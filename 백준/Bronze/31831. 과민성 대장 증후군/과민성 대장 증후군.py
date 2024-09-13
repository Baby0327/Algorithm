"""
과민성 대장 증후군
"""

n, m = map(int, input().split())
stress = list(map(int, input().split()))
total = [stress[0] if stress[0] > 0 else 0]
count = 0 if total[0] < m else 1

for i in range(1, n):
    temp = total[-1] + stress[i]

    if temp > 0:
        total.append(temp)
    else:
        total.append(0)

    if total[-1] >= m:
        count += 1

print(count)