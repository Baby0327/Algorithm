for _ in range(int(input())):
    s = set(list(filter(lambda x : x.isalpha(), input().lower())))
    result = sorted(list(set(chr(97 + i) for i in range(26)) - s))
    print("missing " + "".join(result) if result else "pangram")