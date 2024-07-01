word = input()

for i in word:
    tmp = ord(i)
    print(chr(tmp-32), end="")