n = input()

result = len(n) + n.count(":") + n.count("_")*5
print(result)