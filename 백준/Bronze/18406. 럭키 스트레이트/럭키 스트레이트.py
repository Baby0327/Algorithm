n = [int(i) for i in input()]
i = len(n) // 2
print("LUCKY" if sum(n[:i]) == sum(n[i:]) else "READY")