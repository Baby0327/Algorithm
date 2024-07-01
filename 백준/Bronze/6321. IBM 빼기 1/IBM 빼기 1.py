n = int(input())

for i in range(n):
    computer = input()
    result = ""
    for j in computer:
        tmp = ord(j) + 1
        if tmp == 91:
            tmp = 65
        result += chr(tmp)
    print(f"String #{i+1}")
    print(result)
    print()