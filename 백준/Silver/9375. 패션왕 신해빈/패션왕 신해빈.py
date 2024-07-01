import sys

T = int(sys.stdin.readline())

result = []
for i in range(T):
    n = int(sys.stdin.readline())
    count = []
    cloth = []
    for j in range(n):
        tmp1, tmp2 = sys.stdin.readline().rstrip().split()
        if tmp2 not in cloth:
            cloth.append(tmp2)
            count.append(0)
        count[cloth.index(tmp2)] += 1
        
    total = 1
    for j in count:
        total *= (j+1)

    result.append(total-1)

for i in result:
    print(i)