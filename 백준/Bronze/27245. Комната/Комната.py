n = [int(input()) for _ in range(3)]
mini = min(n[0], n[1])
maxi = max(n[0], n[1])

print("good" if (mini / n[2] >= 2) and (maxi / mini <= 2) else "bad")