symbol = {"animal" : "Panthera tigris", "flower" : "Forsythia koreana", "tree" : "Pinus densiflora"}

while 1:
    s = input()

    if s == "end":
        break
    else:
        print(symbol[s])