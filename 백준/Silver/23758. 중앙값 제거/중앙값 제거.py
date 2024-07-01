import sys
import math

N = int(sys.stdin.readline())
number = list(map(int, sys.stdin.readline().rstrip().split()))
middle = (N+1)//2
number.sort()
count = 0

for i in range(middle):
    count += int(math.log2(number[i]))

print(count+1)