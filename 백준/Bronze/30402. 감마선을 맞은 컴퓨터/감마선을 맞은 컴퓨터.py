word = []
for i in range(15):
    tmp = list(input().split())
    word.append(tmp)

for i in word:
    if "w" in i:
        print("chunbae")
        break
    elif "b" in i:
        print("nabi")
        break
    elif "g" in i:
        print("yeongcheol")
        break