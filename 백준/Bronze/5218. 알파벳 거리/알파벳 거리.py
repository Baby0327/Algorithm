for i in range(int(input())):
    a, b = input().split()
    result = []
    for j in range(len(a)):
        diff = ord(b[j]) - ord(a[j])
        result.append(diff if diff >= 0 else diff + 26)

    print("Distances:", *result)