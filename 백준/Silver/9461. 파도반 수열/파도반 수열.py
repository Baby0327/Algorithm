import sys

T = int(sys.stdin.readline())

P = [1, 1, 1, 2, 2]

for i in range(95):
    P.append(P[i]+P[i+4])

for i in range(T):
    print(P[int(sys.stdin.readline())-1])