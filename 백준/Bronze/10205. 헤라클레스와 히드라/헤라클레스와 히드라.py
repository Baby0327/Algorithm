for n in range(int(input())):
    h = int(input())

    for i in input():
        if i == "c":
            h += 1
        else:
            h -= 1

    print(f"Data Set {n+1}:\n{h}\n")