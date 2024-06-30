import sys

N = int(sys.stdin.readline())
file = list(map(int, sys.stdin.readline().rstrip().split()))
size = int(sys.stdin.readline())

count = 0
for i in file:
    if i == 0:
        continue
    else:
        if i % size == 0:
            count += i//size
        else:
            count += (i//size) + 1

print(size*count)