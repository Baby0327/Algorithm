n = int(input())
s = [int(input())]

if n < 6:
    for i in range(n - 1):
        if s[-1]:
            s.append(0)
        else:
            s.append(1)
    print("\n".join(map(str, s[1:])))
else:
    print("Love is open door")