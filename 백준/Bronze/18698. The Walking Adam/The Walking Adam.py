for _ in range(int(input())):
    s = input()
    print(s.find("D") if s.find("D") != -1 else len(s))