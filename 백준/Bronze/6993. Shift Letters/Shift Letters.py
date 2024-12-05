for i in range(int(input())):
    w, n = input().split()
    print(f"Shifting {w} by {n} positions gives us: {w[len(w) - int(n):] + w[:len(w) - int(n)]}")