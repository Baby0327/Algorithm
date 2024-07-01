import sys

n = int(sys.stdin.readline())

result = []
for i in range(n):
    result.append(int(sys.stdin.readline()))

result.sort()

for i in result:
    sys.stdout.write(str(i)+'\n')