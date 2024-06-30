A, B, C = map(int, input().split())

result = 0

if A == B and B == C:
    print(10000+A*1000)

elif A != B and B != C and C != A:
    result = max(A,B,C)
    print(result*100)

else:
    if A == B:
        result = A
    elif B == C:
        result = B
    else :
        result = A
    print(1000+result*100)