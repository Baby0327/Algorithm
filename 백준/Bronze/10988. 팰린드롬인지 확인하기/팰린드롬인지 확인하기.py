word = list(input())

x = 0
while True:
    if word[x] == word[len(word)-x-1]:
        if x == len(word)//2:
            print(1)
            break
        x += 1
    else:
        print(0)
        break