for i in range(int(input())):
    x, o, y, e, z = input().split()
    print(f"Case {i + 1}: {'YES' if eval(x + o + y) == int(z) else 'NO'}")