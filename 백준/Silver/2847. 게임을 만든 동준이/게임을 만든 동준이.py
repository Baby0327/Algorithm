import sys

N = int(sys.stdin.readline())
result = []

for i in range(N):
    result.append(int(sys.stdin.readline()))

i = len(result)-1
count = 0
while i != 0:
    if result[i] <= result[i-1]:
        result[i-1] -= 1
        count += 1
    else:
        i -= 1

print(count)