for i in range(int(input())):
    s = input()
    print(sum(1 for i in range(len(s)-2) if s[i:i+3] == "WOW"))