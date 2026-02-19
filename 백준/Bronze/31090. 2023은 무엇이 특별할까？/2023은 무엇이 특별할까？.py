for _ in range(int(input())):
    n = input()
    print("Bye" if (int(n) + 1) % int(n[2:]) else "Good")