for _ in range(int(input())):
    name = []
    
    for i in range(int(input())):
        name.append(list(input().split()))

    print(sorted(name, key=lambda x : int(x[0]))[-1][1])