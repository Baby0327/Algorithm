word = list(input())
ABC = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

result = [-1 for i in range(26)]

for i in word:
    for j in ABC:
        if i == j:
            if result[ABC.index(j)] == -1:
                result[ABC.index(j)] = word.index(i)
            else:
                continue

for i in result:
    print(i, end=" ")