import sys
from collections import Counter

N = int(sys.stdin.readline().rstrip())
num = []
result = []

for i in range(N):
    num.append(int(sys.stdin.readline()))

num.sort()

result.append(round(sum(num)/N))
result.append(num[N//2])

count = Counter(num).most_common()

if len(count) > 1 and count[0][1] == count[1][1]:
    result.append(count[1][0])
else:
    result.append(count[0][0])

result.append(max(num)-min(num))

for i in result:
    print(i)
