name = list(input())

test = True
if 97 <= ord(name[0]) <= 122:
    if "_" in name:     # C++ 변수명 -> Java 변수명
        for i in range(len(name)-1):
            if 65 <= ord(name[i+1]) <= 90:
                test = False
                break
            elif name[i] == "_":
                if name[i+1] == "_":
                    test = False
                    break
                else:
                    name[i+1] = chr(ord(name[i+1])-32)
                    name[i] = ""
        if test:
            if name[-1] == "_":
                print("Error!")
            else:
                print("".join(name))
        else:
            print("Error!")

    else:               # Java 변수명 -> C++ 변수명
        for i in range(len(name)):
            if ord(name[i]) <= 90:
                name[i] = "_"+chr(ord(name[i])+32)
        if test:
            print("".join(name))
        else:
            print("Error!")
else:
    print("Error!")