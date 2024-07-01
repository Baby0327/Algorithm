N, A, B = map(int, input().split())

if N > B:
    B = N

if A > B:
    print("Subway")
elif A == B:
    print("Anything")
else:
    print("Bus")