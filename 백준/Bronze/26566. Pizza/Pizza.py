for _ in range(int(input())):
    a, p1 = map(int, input().split())
    r, p2 = map(int, input().split())
    result1 = a / p1
    result2 = (r**2 * 3.141592 ) / p2

    if result1 < result2:
        print("Whole pizza")
    else:
        print("Slice of pizza")