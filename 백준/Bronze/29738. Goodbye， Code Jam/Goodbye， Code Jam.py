for i in range(int(input())):
    n = int(input())

    if n <= 25:
        result = "World Finals"
    elif n <= 1000:
        result = "Round 3"
    elif n <= 4500:
        result = "Round 2"
    else:
        result = "Round 1"

    print(f"Case #{i + 1}: {result}")