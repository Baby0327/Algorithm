import sys

i = 0
while True:
    i += 1
    L, P, V = map(int, sys.stdin.readline().rstrip().split())
    if L == 0 and P == 0 and V == 0:
        break
    result = L*(V//P)
    if V%P > L:
        result += L
    else:
        result += V%P
    print("Case %d:"%i, result)