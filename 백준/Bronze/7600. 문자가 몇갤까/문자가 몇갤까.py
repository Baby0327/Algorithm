while 1:
    s = input().lower()

    if s == "#":
        break

    print(len(list(filter(lambda x : x.isalpha(), list(set(s))))))