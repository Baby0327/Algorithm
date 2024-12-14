for i in range(int(input())):
    s = input()
    result = s[0].lower()

    for j in range(1, len(s)):
        if s[j].isupper():
            result += "_" + s[j].lower()
        else:
            result += s[j]

    print(result)