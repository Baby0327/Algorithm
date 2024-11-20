change = {"a" : "4", "e" : "3", "i" : "1", "o" : "0", "s" : "5"}
s = input()

for i in s:
    print(change.get(i, i), end="")