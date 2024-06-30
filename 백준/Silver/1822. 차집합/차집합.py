import sys

A, B = map(int, sys.stdin.readline().rstrip().split())
A_num = set()
B_num = set()
A_num.update(list(map(int, sys.stdin.readline().rstrip().split())))
B_num.update(list(map(int, sys.stdin.readline().rstrip().split())))

result = A_num-B_num
print(len(result))

if len(result) != 0:
    result = sorted(result)
    for i in result:
        print(i, end=" ")