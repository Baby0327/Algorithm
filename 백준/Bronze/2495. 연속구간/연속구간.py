for _ in range(3):
    n = input()
    l = 1
    result = []

    for i in range(8):
        if 0 < i < 8 and n[i] == n[i - 1]:
            l += 1
        else:
            result.append(l)
            l = 1
            
    result.append(l)
    print(max(result))