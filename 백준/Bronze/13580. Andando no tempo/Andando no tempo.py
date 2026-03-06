n  = sorted(list(map(int, input().split())))
print("S" if n[0] == n[1] or n[1] == n[2] or n[2] - n[1] - n[0] == 0 else "N")