t1, e1, f1 = map(int, input().split())
t2, e2, f2 = map(int, input().split())

MAX = t1*3 + e1*20 + f1*120
MEL = t2*3 + e2*20 + f2*120

if MAX > MEL:
    print("Max")
elif MAX < MEL:
    print("Mel")
else:
    print("Draw")