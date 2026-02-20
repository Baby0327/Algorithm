n = [int(input()) for _ in range(4)]

if n.count(n[0]) == len(n):
    print("Fish At Constant Depth")
elif len(set(n)) == 4:
    if n == sorted(n):
        print("Fish Rising")
    elif n == sorted(n, reverse=True):
        print("Fish Diving")
    else:
        print("No Fish")
else:
    print("No Fish")