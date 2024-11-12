while 1:
    s = input()

    if s == "*":
        break
        
    if len(set(s) - {" "}) == 26:
        print("Y")
    else:
        print("N")