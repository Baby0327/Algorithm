while True:
    word = input()
    if word == "END":
        break
    result = "".join(reversed(word))
    print(result)