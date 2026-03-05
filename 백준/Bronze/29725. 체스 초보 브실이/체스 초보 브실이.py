s = {"." : 0, "k" : 0, "K" : 0, "p" : 1, "P" : 1, "n" : 3, "N" : 3, "b" : 3, "B" : 3, "r" : 5, "R" : 5, "q" : 9, "Q" : 9}
total = 0

for _ in range(8):
    for c in input():
        if ord(c) > 97:
            total -= s[c]
        else:
            total += s[c]

print(total)