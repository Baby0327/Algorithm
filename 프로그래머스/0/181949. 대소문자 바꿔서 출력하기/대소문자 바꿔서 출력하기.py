str = input()
answer = ""
for i in str:
    if ord(i) >= 97:
        answer += chr(ord(i)-32)
    else:
        answer += chr(ord(i) + 32)
print(answer)