import sys

N = int(sys.stdin.readline())
N_num = set(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
M_num = list(map(int, sys.stdin.readline().split()))

for i in M_num:
    if i in N_num:
        print('1')
    else:
        print('0')