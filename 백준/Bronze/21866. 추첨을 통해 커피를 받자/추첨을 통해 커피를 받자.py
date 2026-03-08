n = list(map(int, input().split()))

if sum(n) < 100:
    print("none")
elif len([i for i in range(9) if n[i] > (i // 2) * 100 + 100]) > 0:
    print("hacker")
else:
    print("draw")