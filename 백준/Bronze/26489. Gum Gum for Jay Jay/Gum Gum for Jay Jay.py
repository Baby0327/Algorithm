count = 0

while 1:
    try:
        input()
        count += 1
    except EOFError:
        print(count)
        break