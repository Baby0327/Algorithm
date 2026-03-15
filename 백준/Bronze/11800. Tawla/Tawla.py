for i in range(int(input())):
    b, a = sorted(map(int, input().split()))
    dice = ["Yakk", "Doh", "Seh", "Ghar", "Bang", "Sheesh"]
    same = ["Habb Yakk", "Dobara", "Dousa", "Dorgy", "Dabash", "Dosh"]

    if a == b:
        result = same[a - 1]
    else:
        result = dice[a - 1] + " " + dice[b - 1]

        if result == "Sheesh Bang":
            result = "Sheesh Beesh"

    print(f"Case {i + 1}: {result}")