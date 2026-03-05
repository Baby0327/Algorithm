Ap, Al = map(int, input().split())
Bp, Bl = map(int, input().split())

while Al > 0 and Bl > 0:
    Al -= Bp
    Bl -= Ap

if Al > 0:
    print("PLAYER A")
elif Bl > 0:
    print("PLAYER B")
else:
    print("DRAW")